import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
queue = deque()

# 이동 가능 방향은 오른쪽 or 아래
dir = [[0, 1], [1, 0]]

def BFS(x, y):
  visited[x][y] = True
  queue.append((x, y))

  while queue:
    curX, curY = queue.popleft()

    if graph[curX][curY] == -1:
      return
    
    for d in dir:
      # 현재 노드에서 오른쪽 or 아래의 점프 가능 칸 수 탐색
      nextX = curX + d[0] * graph[curX][curY]
      nextY = curY + d[1] * graph[curX][curY]

      if nextX >= 0 and nextY >= 0 and nextX < n and nextY < n:
        if visited[nextX][nextY] == False:
          visited[nextX][nextY] = True
          queue.append((nextX, nextY))
      

BFS(0, 0)

if visited[n - 1][n - 1] == False:
  print("Hing")
else:
  print("HaruHaru")

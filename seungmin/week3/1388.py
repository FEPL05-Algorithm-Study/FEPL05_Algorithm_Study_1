import sys
from collections import deque
sys.setrecursionlimit(10**6)  # 1,000,000까지 허용

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
visited = [[0] * m for _ in range(n)]
result = 0

def DFS(cnt, x, y):
  # 같은 구역을 탐색하기 위해 구역 번호를 매김
  visited[x][y] = cnt

  if graph[x][y] == '-':
    if y + 1 < m and graph[x][y + 1] == '-':
      DFS(cnt, x, y + 1)
  else:
    if x + 1 < n and graph[x + 1][y] == '|':
      DFS(cnt, x + 1, y)

for _ in range(n):
  graph.append(list(map(str, input().strip())))

for i in range(n):
  for j in range(m):
    if not visited[i][j]:
      result += 1
      DFS(result, i, j)

print(result)

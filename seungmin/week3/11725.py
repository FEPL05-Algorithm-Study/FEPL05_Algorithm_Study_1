import sys
from collections import deque
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
visited = [False] * (n + 1)
graph = defaultdict(list)
q = deque()
ans = [0] * (n + 1)

for _ in range(n - 1):
  v, u = map(int, input().split())
  graph[v].append(u)
  graph[u].append(v)


def BFS(start):
  visited[start] = True
  q.append(start)

  while q:
    cur = q.popleft()

    for next in graph[cur]:
      # 각 노드의 부모를 저장
      if not visited[next]:
       ans[next] = cur
       visited[next] = True
       q.append(next)

BFS(1)

for i in range (2, n + 1):
  print(ans[i])

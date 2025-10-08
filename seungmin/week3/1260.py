import sys
from collections import defaultdict

input = sys.stdin.readline


visitedDFS = [False] * 1001
visitedBFS = [False] * 1001

graph = defaultdict(list)

# 스택을 활용한 DFS
def DFS(startNode):
  stack = [startNode]
  visitedDFS[startNode] = True

  while stack:
    curNode = stack.pop()
    print(curNode, end = ' ')

    for nextNode in reversed(graph[curNode]):
      if not visitedDFS[nextNode]:
        visitedDFS[nextNode] = True
        stack.append(nextNode)


# 재귀를 이용한 DFS
def DFS_R(startNode):
  visitedDFS[startNode] = True
  print(startNode, end=' ')
  for nextNode in graph[startNode]:
    if not visitedDFS[nextNode]:
      DFS_R(nextNode)
  
  
def BFS(startNode):
  queue = [startNode]
  visitedBFS[startNode] = True

  while queue:
    curNode = queue.pop(0) # list에서 pop할 위치의 index가 인자로 들어가야 맨 앞의 요소만 꺼낼 수 있다.
    print(curNode, end = ' ')
    for nextNode in graph[curNode]:
      if not visitedBFS[nextNode]:
        queue.append(nextNode)
        visitedBFS[nextNode] = True
  

n, m, v = map(int, input().split())


for _ in range(m):
  node, adjacentNode = map(int, input().split())
  graph[node].append(adjacentNode)
  graph[adjacentNode].append(node)

# 문제 조건 : 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
for node in graph:
  graph[node].sort()


DFS_R(v)
print()
BFS(v)


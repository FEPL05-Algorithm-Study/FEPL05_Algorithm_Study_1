import sys
from collections import deque
input = sys.stdin.readline


n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
# 그래프 생성
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 연결된 정점 번호 정렬
for i in range(n+1):
    graph[i].sort()



# dfs 구현
visited = [0]*(n+1)

def dfs(cur):
    if visited[cur]:
        return
    
    print(cur, end=' ')

    visited[cur] = 1
    for next in graph[cur]:
        dfs(next)


# bfs 구현
def bfs(start):
    visited = [0]*(n+1)
    q = deque([start])
    visited[start] = 1

    while q:
        cur = q.popleft()

        print(cur, end=' ')

        for next in graph[cur]:
            if not visited[next]:
                visited[next] = 1
                q.append(next)


dfs(v)
print('')
bfs(v)
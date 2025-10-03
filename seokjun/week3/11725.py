import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
# 그래프 생성
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 방분여부 체크, 부모노드 저장 배열 생성
visited = [0]*(n+1)
parents = [0]*(n+1)

# dfs로 구현
def dfs(cur):
    # 방문했다면 종료
    if visited[cur]:
        return
    
    visited[cur] = 1

    for next in graph[cur]:
        # 처음 방문시 부모노드 갱신
        if not parents[next]:
            parents[next] = cur
        dfs(next)

# bfs로 구현
def bfs(cur):
    q = deque([cur])
    visited[cur] = 1

    while q:
        cur = q.popleft()

        for next in graph[cur]:
            if not visited[next]:
                visited[next] = 1
                # 방문시 부모노드 갱신
                parents[next] = cur
                q.append(next)


# dfs(1)
bfs(1)
print('\n'.join(map(str,parents[2:])))
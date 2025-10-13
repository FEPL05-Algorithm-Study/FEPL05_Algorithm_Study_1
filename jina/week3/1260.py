import sys

def dfs(idx):
    global visited
    visited[idx] = True  # 방문표시
    print(idx, end = ' ') 
    for next in range(1, N+1):

        # 방문된 적 없고, 현재 idx 노드에서 갈 수 있다면 dfs 수행
        if not visited[next] and graph[idx][next]:
            dfs(next)

def bfs():
    global q, visited
    while q: # q가 빌 때까지
        cur = q.pop(0)
        visited[cur] = True
        print(cur, end = ' ')

        # cur 부터 갈 수 있는 모든 노드들을 q 뒤에 push
        for next in range(1, N+1):
            # 방문된 적 없고, 현재 cur 노드에서 갈 수 있다면 방문 표시
            if not visited[next] and graph[cur][next]:
                
                # 방문하겠다 = q에 추가하겠다
                visited[next] = True
                q.append(next)


input = sys.stdin.readline
N, M, V = map(int, input().split())

graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

# dfs
dfs(V)
print()

# bfs
visited = [False] * (N+1) # 모두 초기화
q = [V]
bfs()
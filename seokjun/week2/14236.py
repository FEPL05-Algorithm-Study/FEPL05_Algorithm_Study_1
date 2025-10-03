# https://www.acmicpc.net/problem/14236

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]


edges = []
# 모든 명제들을 배열에 저장후 난이도 기준으로 정렬
for i in range(n):
    for j in range(n):
        if i!=j:
            edges.append((arr[i][j], i, j))

edges.sort()


def dfs(graph, node, visited):
    visited[node] = True
    for next in graph[node]:
        if not visited[next]:
            dfs(graph, next, visited)

# SSC여부를 판별하는 함수
def valid(L, R):
    graph = [[] for _ in range(n)]
    rev = [[] for _ in range(n)]

    for w,x,y in edges[L:R+1]:
        graph[x].append(y)
        rev[y].append(x)

    visited = [False]*n
    dfs(graph, 0, visited)
    if not all(visited): return False

    visited = [False]*n
    dfs(rev, 0, visited)
    if not all(visited): return False

    return True


# 정렬된 명제들을 투포인터로 최솟값 계산
answer = float('inf')
L = 0 
for R in range(len(edges)):
    while L<=R and valid(L,R):
        answer = min(answer, edges[R][0]-edges[L][0])
        L += 1

print(answer if answer != float('inf') else 0)










# answer = 200000

# visited = [[False for _ in range(n)] for _ in range(n)] 

# def valid(route):
#     graph = [[] for _ in range(n)]
#     check = [[False for _ in range(n)] for _ in range(n)]

#     for x,y in route:
#         graph[x].append(y)

#     for i in range(n):
#         q=deque([i])
#         visited = [[False for _ in range(n)] for _ in range(n)]
#         visited[i][i] = True

#         while q:
#             cur = q.popR()

#             check[i][cur] = True

#             for next in graph[cur]:
#                 if visited[cur][next]: continue
#                 visited[cur][next] = True
#                 q.append(next)

#     cnt = 0
#     for i in range(n):
#         for j in range(n):
#             cnt += int(check[i][j])

#     return [cnt == n**2, check]


# def dfs(x,y,curMin,curMax,route):
#     global visited, answer

#     if valid(route)[0]:
#         answer = min(answer,curMax-curMin)
#         return

#     cur = y
#     for next in range(n):
#         if next == cur: continue
#         if visited[cur][next]: continue

#         visited[cur][next] = True

#         LMin = min(curMin,arr[cur][next])
#         LMax = max(curMax,arr[cur][next])

#         route.append([cur,next])

#         dfs(cur,next,LMin, LMax,route)

#         route.pop()

#         visited[cur][next] = False

#     return


# for i in range(n):
#     for j in range(n):
#         if i==j: continue

#         visited = [[False for _ in range(n)] for _ in range(n)]
        
#         visited[i][j] = True

#         dfs(i,j,arr[i][j],arr[i][j],[[i,j]])

# print(answer)
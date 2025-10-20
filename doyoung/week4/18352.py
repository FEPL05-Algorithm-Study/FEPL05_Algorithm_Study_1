from collections import deque
import sys

input = sys.stdin.readline  
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
# 도시 그리기

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
# 단방향 도로 저장



distance = [-1] * (n + 1)
# 모든 도시를 방문하지 않은것으로 초기값 설정

distance[x] = 0
# 출발 도시 거리는 0으로 설정

q = deque([x]) 

while q:
    now = q.popleft()  

    # 현재 도시와 연결된 도시 탐색
    for next_city in graph[now]:  
        if distance[next_city] == -1:  
            distance[next_city] = distance[now] + 1  
            q.append(next_city)  


check = False # 해가 없을경우 체크

for i in range(1, n + 1):
    if distance[i] == k:  # k에 맞는 도시 출력
        print(i)
        check = True


if check == False:
    print(-1)

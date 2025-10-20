import heapq
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

# 그래프 인접 리스트
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))  # 비용이 항상 1

# 거리 배열 초기화
INF = float('inf')
distance = [INF] * (N + 1)
distance[X] = 0

# 다익스트라 알고리즘
heap = [(0, X)]
while heap:
    dist, now = heapq.heappop(heap)

    # 이미 처리된 거리보다 크면 무시
    if distance[now] < dist:
        continue

    for next_node, cost in graph[now]:
        new_dist = dist + cost
        if new_dist < distance[next_node]:
            distance[next_node] = new_dist
            heapq.heappush(heap, (new_dist, next_node))

# 결과 출력
found = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        found = True

if not found:
    print(-1)

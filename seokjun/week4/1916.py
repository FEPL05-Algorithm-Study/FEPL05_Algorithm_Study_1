import sys
from collections import defaultdict
from heapq import heappop,heappush
input = sys.stdin.readline

n = int(input())
m = int(input())
edges = [list(map(int, input().split())) for _ in range(m)]
start,end = map(int, input().split())

graph = defaultdict(list)

# 그래프 생성
for a,b,w in edges:
    graph[a].append((b,w))

# 다익스트라를 사용해 최단경로 탐색
heap = [(0,start)]
d = [10**16] * (n+1) # 최단경로를 저장할 배열
d[start] = 0

while heap:
    # 탐색하지 않은 노드중 거리가 가장 작은 노드 선택
    dist, cur = heappop(heap)

    # 이미 저장된 최단경로보다 길다면 종료
    if dist > d[cur]:
        continue

    for next,w in graph[cur]:
        # 현재노드를 거쳐 다음노드로 가는 경로가 현재 저장된 다음노드의 최단경로보다 짧다면 힙에 추가 
        if d[next] > d[cur] + w:
            d[next] = d[cur] + w
            heappush(heap,(d[next],next))

print(d[end])

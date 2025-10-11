import sys
from collections import defaultdict
from heapq import heappop, heappush
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# 그래프 생성
graph = defaultdict(list)

for a,b in edges:
    graph[a].append(b)

# 다익스트라를 통한 최단경로 찾기
heap = [(0,x)]
d = [10**16] * (n+1)
d[x] = 0

while heap:
    dist, cur = heappop(heap)

    # 이미 저장된 경로보다 길면 종료
    if dist > d[cur]:
        continue

    for next in graph[cur]:
        # cur을 거쳐서 next로 가는 경로가 현재 저장된 next까지의 경로보다 짧다면 업데이트
        if d[next] > d[cur] + 1:
            d[next] = d[cur] + 1
            heappush(heap,(d[next], next))

# 최당경로가 k인 노드만 추출하고 정렬
arr = [x for x in range(1,n+1) if d[x] == k]
arr.sort()
print('\n'.join(map(str,arr)) if arr else -1)

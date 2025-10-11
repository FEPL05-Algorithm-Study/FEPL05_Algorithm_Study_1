import sys
from collections import defaultdict
input = sys.stdin.readline

v, e = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(e)]

# 간선을 가중치가 작은 순으로 정렬
edges.sort(key=lambda x:x[2])

# 유니온 파인드를 사용해 가중치가 가장 작은간선부터 추가해 나감
parents = [x for x in range(v+1)]
level = [0] * (v+1)

def find(n):
    if parents[n] != n:
        parents[n] = find(parents[n])
    return parents[n]

def union(a,b):
    a = find(a)
    b = find(b)

    if level[a] > level[b]:
        parents[b] = a
    elif level[a] < level[b]:
        parents[a] = b
    else:
        level[a] += 1
        parents[b] = a

answer = 0

for a,b,w in edges:
    # 가중치가 가장 작은 간선부터 간선추가
    # 간선이 추가된다면 a와 b를 같은 집합에 추가
    # 만약 모든 노드가 연결되게 되면 find(a)==find(b) 가 됨
    if find(a) != find(b):
        answer += w
        union(a,b)

print(answer)
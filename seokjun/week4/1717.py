import sys
input = sys.stdin.readline

n, m = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(m)]

parents = [x for x in range(n+1)]
level = [0] * (n+1)

# 루트 노드를 찾으며 경로 압축
# 항상 부모노드의 인덱스는 루트노드로 업데이트됨
def find(n):
    if parents[n] != n:
        parents[n] = find(parents[n])
    return parents[n]

# a와 b를 하나의 그룹으로 합침
def union(a,b):
    # 각각의 루트노드를 찾음
    a = find(a)
    b = find(b)

    # a트리의 깊이가 더 깊다면, b의 부모를 a로(b를 a트리 밑에 붙임)
    if level[a] > level[b]:
        parents[b] = a

    # b트리의 깊이가 더 깊다면, a의 부모를 b로(a를 b트리 밑에 붙임)
    elif level[a] < level[b]:
        parents[a] = b

    # 만약 두 트리의 깊이가 같다면, a트리의 깊이를 1늘리고 b를 a트리 밑에 붙임
    else:
        level[a] += 1
        parents[b] = a

for q,a,b in query:
    if q:
        # 만약 a의 루트노드와 b의 루트노드가 같다면 동일 집합
        print('YES' if find(a) == find(b) else 'NO')
    else:
        union(a,b)

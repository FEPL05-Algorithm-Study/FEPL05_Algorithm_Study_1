import sys
from collections import deque


input = sys.stdin.readline

N = int(input())
vertices = [[] for _ in range(N + 1)]  # 빈 노드 배열생성
parent = [0] * (N + 1) # 미리 부모 배열생성

# 인접한 노드 담기
for _ in range(N - 1):
    a, b = map(int, input().split())
    vertices[a].append(b)
    vertices[b].append(a)


q = deque()
q.append(1)

# 노드 부모 찾기 실행
while q:
    current = q.popleft()
 
    for v in vertices[current]: 
        
        if parent[v] == 0: 
            parent[v] = current  
            q.append(v) 

print('\n'.join(map(str, parent[2:])))
  

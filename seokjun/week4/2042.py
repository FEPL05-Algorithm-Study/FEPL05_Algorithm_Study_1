import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
query = [list(map(int, input().split())) for _ in range(m+k)]

# 세그먼트 트리의 리프노드의 개수는 n이상의 2의 제곱수
# size 는 n 이상의 2^k
size = 1
while size < n:
    size *= 2

# 세그먼트 트리의 전체길이는 2^(k+1) - 1이므로 size*2
segtree = [0] * (size*2)

# 리프노드는 배열의 각 요소
for i in range(n):
    segtree[i+size] = arr[i]

# 부모노드는 왼쪽자식노드(인덱스 2*i)와 오른쪽자식노드(인덱스 2*i+1)의 합
for i in range(size-1,0,-1):
    segtree[i] = segtree[2*i] + segtree[2*i + 1]

# 리프노드부터 부모노드를 거슬러 올라가며 변경값 업데이트
def update(b,c):
    b += size
    diff = c - segtree[b]
    # b가 루트노드일때까지 변경값을 업데이트 해준다
    while b>0:
        segtree[b] += diff
        b //= 2 

# left,right사이의 합을구함
def get_sum(b,c):
    result = 0
    left = b + size
    right = c + size
    while left<=right:
        # 만약 왼쪽자식노드가 홀수라면, 해당노드의 부모노드는 범위 밖이다
        # 미리 값을 더해주고 한칸 으론쪽으로 옮김 
        if left % 2 == 1:
            result += segtree[left]
            left += 1

        # 만약 오른쪽자식노드가 짝수라면, 해당노드의 부모노드는 범위 밖이다
        # 미리 값을 더해주고 한칸 왼쪽으로 옮김 
        if right % 2 == 0:
            result += segtree[right]
            right -= 1

        # 부모노드로 이동 
        left //= 2
        right //= 2
    
    return result

answer = []

for a,b,c in query:
    if a == 1:
        update(b-1,c)
    elif a == 2:
        answer.append(get_sum(b-1,c-1))

print('\n'.join(map(str,answer)))
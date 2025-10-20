import sys

input = sys.stdin.readline

N, M, V = map(int, input().strip().split())
arr = [int(input().strip()) for _ in range(N)]
questions = [list(map(int, input().split())) for _ in range(M+V)]
answer = []

# 세그먼트 트리 초기화
size = 1
while size < N:
    size *= 2

segArr = [0] * (2 * size)

def segTree():
    for i in range((N)):
        segArr[size+i] = arr[i]
    
    for i in range(size-1, 0, -1):
        segArr[i] = segArr[i*2] + segArr[i*2+1]

def query(b, c):
    answer = 0

    left = b + size
    right = c + size

    while left <= right:
        if left % 2 == 1:
            answer += segArr[left]
            left += 1

        if right % 2 == 0:
            answer += segArr[right]
            right -= 1

        left //= 2
        right //= 2
    
    return answer

def update(m ,v):
    m += size
    diff = v - segArr[m]

    while m > 0:
        segArr[m] += diff
        m //= 2

segTree()

for a, b, c in questions:
    if a == 1:
        update(b-1, c)
    elif a == 2:
        answer.append(query(b-1, c-1))

print('\n'.join(map(str, answer)))
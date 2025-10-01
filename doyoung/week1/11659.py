import sys

input = sys.stdin.readline

value = list(map(int, input().split()))
N = value[0]
M = value[1]
numbers = list(map(int, input().split()))
prev_sum = []


# 구간합 미리 만들기
for i, item in enumerate(numbers):
    if i == 0:
        prev_sum.append(item)
        continue
    
    prev_sum.append(prev_sum[i - 1] + item)

# 필요한 구간합 출력하기
for i in range(M):
    target = list(map(int, input().split()))

    left = target[1] - 1
    right =  target[0] - 2

    print(prev_sum[left] - (0 if target[0] == 1 else prev_sum[right]))
    


import sys

N = int(sys.stdin.readline())

arr = []

# 입력값 list로 만들기
for i in range(N):
    input = int(sys.stdin.readline())
    arr.append(input)

# 정렬후 바로 출력
for j in sorted(arr):
    print(j)
    
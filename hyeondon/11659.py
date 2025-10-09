import sys
input = sys.stdin.readline

number, count = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합 배열 (prefix sum)
prefix = [0] * (number + 1)

for i in range(1, number + 1):
    prefix[i] = prefix[i-1] + arr[i-1]

if len(arr) == number:
    for _ in range(count):
        A, B = map(int, input().split())
        print(prefix[B] - prefix[A-1])

import sys

input = sys.stdin.readline


N = int(input())
count, sum, start = 0, 0, 1 # 출력, 비교, 시작 변수설정

# 투포인터 로직으로 N과 일치하면 count 증가
for i in range(1, N):
    sum += i

    while sum > N:
        sum -= start
        start += 1

    if sum == N:
        count += 1

print(count + 1)
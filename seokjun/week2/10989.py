import sys
input = sys.stdin.readline

n = int(input())

# 중복된 숫자가 메모리를 사용하지않게 딕셔너리에 개수저장
d = {}
for _ in range(n):
    a = int(input())
    if a in d:
        d[a] += 1
    else:
        d[a] = 1

arr = list(d.keys())
arr.sort()

for x in arr:
    for _ in range(d[x]):
        print(x)
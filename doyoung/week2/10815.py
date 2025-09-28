import sys

input = sys.stdin.readline

N = int(input())
my_card = set(input().split()) # 빠르게 비교해야 하므로 집합으로 받음
M = int(input())
numbers = input().split()

result = []

# 카드가 있으면 1, 없으면 0 추가
for i in numbers:
    if i in my_card:
        result.append('1')
    else:
        result.append('0')

# 표기에 맞춰서 출력
print(" ".join(result))

    

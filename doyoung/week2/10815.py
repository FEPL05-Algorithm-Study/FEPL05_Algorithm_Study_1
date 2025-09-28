import sys

try:
    # 'input.txt' 파일을 읽기 모드('r')로 열고
    # sys.stdin을 이 파일 핸들로 대체합니다.
    sys.stdin = open('input.txt', 'r')
except FileNotFoundError:
    # input.txt 파일이 없을 경우 예외 처리
    pass

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

    

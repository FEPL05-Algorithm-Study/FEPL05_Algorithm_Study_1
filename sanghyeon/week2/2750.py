import sys

# 로컬 테스트용 - 제출할 때는 이 줄들을 주석 처리
# sys.stdin = open('input.txt', 'r') # input.txt 파일을 읽어옴
# sys.stdout = open('output.txt', 'w') # output.txt 파일을 출력

# 빠른 입력
input = sys.stdin.readline

# 입력 받기
n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

# 버블 정렬
for i in range(n):
    for j in range(0, n - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

# 출력
for num in array:
    print(num)



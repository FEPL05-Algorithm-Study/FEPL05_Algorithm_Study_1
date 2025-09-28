import sys

N = int(sys.stdin.readline())

for i in range(N):
    input = sys.stdin.readline().split()
    to_int = list(map(int, input)) # 입력값 int 변환
    to_int.sort() # 정렬
    print(to_int[-3]) # 3번째 높은수 출력
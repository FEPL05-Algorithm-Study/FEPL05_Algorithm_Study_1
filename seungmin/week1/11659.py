import sys

# input = sys.stdin.readline 등으로 초기화가 가능하다.
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
sum = [0]
tmp = 0

for i in numbers:
    tmp = tmp + i
    # numbers의 각 요소와 이전 요소와의 합 -> 구간합 구하기
    sum.append(tmp)

for i in range(m):
    # input()의 경우 sys.stdin.readline() 대비 10배 이상 느리다
        #why - prompt 출력 때문에 시간 지연
    # m이 최대 100,000일 수 있기 때문에 100,000번의 input() 호출은? 느리다~
    start, end = map(int, input().split())
    print(sum[end] - sum[start - 1])

import sys

input = sys.stdin.readline

N, M = map(int,  input().split())

# '|'의 경우 아래에 있는지 확인할때 첫째줄인 경우에 마지막을 탐색해서 범위를 벗어나므로 더미데이터를 위에 추가 
# ex) list[-1] 을 탐색하면 끝의 데이터가 탐색됨
pattern = [[0] * M] 
count = 0
now = ''

# 장판 무늬를 2차원 배열로 만듬
for _ in range(N):
    pattern.append(' '.join(input()).split())


for i in range(N + 1):
    for j in range(M):
        # 마지막이 '-'로 끝나면 체크하기 위해 저장
        now = pattern[i][j] 

        # '-'인 경우에 범위를 벗어나지 않고 다음값이 '-' 아니면 count +1
        if pattern[i][j] == '-' and j + 1 < M and not pattern[i][j + 1] == '-':
            count += 1

        # '|'인 경우에 '|' 아래에 연속적이지 않은 경우에 count +1
        if pattern[i][j] == '|' and not pattern[i - 1][j] == '|':
            count += 1

    # 한줄이 '-' 로 끝나면 count +1
    if now == '-':
        count += 1


print(count)


        
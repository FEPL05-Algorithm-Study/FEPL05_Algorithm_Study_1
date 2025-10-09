import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))
sheet = []
target = []
prev_sum = [[0] * (N + 1) for _ in range(N + 1)]  # 문제에 좌표 그대로 쓰기위해 N + 1 배열 초기화 

# 예제 입력값 배열로 만들기
for i in range(N):
    sheet.append(list(map(int, input().split())))

# 2차원 배열 누적합 계산하기
for i, item in enumerate(sheet, start = 1) :
    for j, value in enumerate(item, start = 1):
        prev_sum[i][j] = prev_sum[i-1][j] + prev_sum[i][j-1] - prev_sum[i-1][j-1] + sheet[i - 1][j - 1]
    
# 좌표에 따른 구간합 구하기
for i in range(M):
    x1, y1, x2, y2 = list(map(int, input().split()))    
    
    right_sum = prev_sum[x2][y2] - prev_sum[x1 - 1][y2] - prev_sum[x2][y1 - 1] + prev_sum[x1 - 1][y1 - 1]
    print(right_sum)
    


    
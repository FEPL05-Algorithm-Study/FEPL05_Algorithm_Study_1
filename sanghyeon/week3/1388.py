import sys

input = sys.stdin.readline

# DFS 함수 정의
def dfs(x, y, tile): # x = 행, y = 열, tile = 모양('-' 또는 '|')
    # 현재 칸 방문 처리(방문 = True, 비방문 = False)
    visited[x][y] = True
    
    # 방향 설정: 문자에 따라 다른 방향으로만 탐색
    if tile == '-':
        # 가로 판자: 좌우만 탐색
        directions = [(0, -1), (0, 1)]  # 왼쪽, 오른쪽
    elif tile == '|':
        # 세로 판자: 상하만 탐색
        directions = [(-1, 0), (1, 0)]  # 위, 아래
    
    # 인접한 칸 탐색
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        
        # 범위 내에 있고, 방문하지 않았고, 같은 문자인 경우
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and board[nx][ny] == tile:
                dfs(nx, ny, tile)

# 입력값 받기
n, m = map(int, input().split()) 
board = []

for _ in range(n):
    board.append(list(input().strip())) 

# 방문 배열 초기화 (False로 채움)
visited = [[False] * m for _ in range(n)]

# 판자 개수 카운트
count = 0

# 모든 칸을 순회
for i in range(n):
    for j in range(m):
        # 아직 방문하지 않은 칸의 경우
        if not visited[i][j]:
            dfs(i, j, board[i][j])
            count += 1

#결과 출력
print(count)

from collections import deque
import sys

input = sys.stdin.readline

N = int(input())


gamp_map = []  # 게임 구역
visit = [] # 방문 표시

# N으로 게임구역을 만들고, 그 크기만큼 False로 visit을 채움
for _ in range(N):
    gamp_map.append(list(map(int, input().split())))
    visit.append([False] * N)

# 아래, 오른쪽 으로 이동하기 위한 방향성
dx = [1, 0]
dy = [0, 1]

def bfs(x, y):
    # deque를 만들고 첫 x, y를 기록하고 방문했다고 기록
    queue = deque()
    queue.append((x, y))
    visit[x][y] = True

    while queue:
        # x, y 값을 마지막 방문 좌표값으로 셋팅
        x, y = queue.popleft()

        if gamp_map[x][y] == -1:
            return 'HaruHaru'
        
        jump = gamp_map[x][y]

        for i in range(2):
            # 0 일때는 아래로 이동, 1일때는 오른쪽으로 이동
            nx = x + dx[i] * jump
            ny = y + dy[i] * jump
            
            # 0보다 크고 게임 최대 크기인 N 보다 작고 방문하지 않은 좌표면 방문으로 체크하고 좌표에 넣음
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0:
                visit[nx][ny] = True
                queue.append((nx, ny))
    
    return 'Hing'


print(bfs(0, 0))
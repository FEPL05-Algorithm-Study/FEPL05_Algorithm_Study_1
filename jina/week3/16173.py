from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

# 오른쪽 이동만 가능 
dx = [1, 0]

# 왼쪽 이동만 가능
dy = [0, 1]

def bfs(x, y):
    q = deque()
    q.append([x, y])

    while q: 
        x, y = q.popleft()
        # 쩰리가 현재 밟고 있는 칸의 숫자만큼 점프해야함
        step = graph[x][y]

        # 끝점이 -1이므로 도달하면 성공
        if graph[x][y] == -1:
            return True
        
        # 쩰리가 현재 밟고 있는 숫자와 이동수 곱하여 이동하기
        for move in range(2): # 두 방향으로 시도
            nx = x + dx[move]*step
            ny = y + dy[move]*step
            print('nx, ny: ', nx, ny)
            # 주어진 범위 벗어나면 무시
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            # 방문하지 않았다면
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append([nx, ny])

if bfs(0, 0):
    print('HaruHaru')
else: 
    print('Hing')


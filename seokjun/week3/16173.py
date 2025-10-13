import sys
sys.setrecursionlimit(10**6)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

answer = 'Hing'

dx = [1,0]
dy = [0,1]

# 방문여부 체크 배열
visited = [[0]*n for _ in range(n)]

def dfs(x,y):
    global answer
    # 범위를 벗어낫거나 방문했으면 종료
    if x<0 or x>=n or y<0 or y>=n or visited[x][y]:
        return

    visited[x][y] = 1

    # 목적지 도달시 종료
    if x==n-1 and y==n-1:
        answer = 'HaruHaru'
        return
    
    # 해당칸에 쓰여진 수만큼 이동
    step = board[x][y]
    for i in range(2):
        nx,ny = x+dx[i]*step, y+dy[i]*step
        dfs(nx,ny)

dfs(0,0)

print(answer)
        

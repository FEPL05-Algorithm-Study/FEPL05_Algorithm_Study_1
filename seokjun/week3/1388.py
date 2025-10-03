import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
board = [[x for x in input()] for _ in range(n)]

visited = [[0]*m for _ in range(n)]

def dfs(x,y,shape):
    # 범위 밖이거나 모양이 다르면 종료
    if x<0 or x>=n or y<0 or y>=m or visited[x][y] or board[x][y]!=shape:
        return
    
    visited[x][y] = 1

    # '-' 모양이면 동,서만 탐색 '|'모양이면 남,북만 탐색
    dx,dy = [0,1] if shape == '-' else [1,0]
    nx,ny = x+dx,y+dy
    dfs(nx,ny,shape)

answer = 0

# 체크되지 않은 모든 칸에서 dfs탐색
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i,j,board[i][j])
            answer += 1

print(answer)
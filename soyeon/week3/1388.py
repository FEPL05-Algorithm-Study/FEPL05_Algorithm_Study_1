import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
count = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]: 
            shape = board[i][j] 
            visited[i][j] = True

            if shape == '-': # 기호가 얼마나 더 이어져 있는지 확인해서 visited에 반영하기 위한 조건문
                k = j + 1
                while k < m and board[i][k] == '-':
                    visited[i][k] = True
                    k += 1

            elif shape == '|':               
                k = i + 1
                while k < n and board[k][j] == '|':
                    visited[k][j] = True
                    k += 1

            count += 1 
            
print(count)
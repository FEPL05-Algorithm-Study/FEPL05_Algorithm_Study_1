import sys
from collections import deque

def main():
    input = sys.stdin.readline
    N = int(input().strip())
    board = [list(map(int, input().split())) for _ in range(N)]

    # BFS
    q = deque([(0, 0)])
    visited = [[False]*N for _ in range(N)]
    visited[0][0] = True

    while q:
        r, c = q.popleft()

        if board[r][c] == -1:
            print("HaruHaru")
            return

        jump = board[r][c]
        if jump == 0:  
            continue

        # 오른쪽으로 이동
        nr, nc = r, c + jump
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            visited[nr][nc] = True
            q.append((nr, nc))

        # 아래로 이동
        nr, nc = r + jump, c
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            visited[nr][nc] = True
            q.append((nr, nc))

    print("Hing")

if __name__ == "__main__":
    main()

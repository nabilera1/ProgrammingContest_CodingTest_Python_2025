# 구슬 탈출 2

from collections import deque

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# R, B 위치 찾기
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

# 굴리는 함수: 구슬이 벽이나 구멍 만날 때까지 이동
def move(x, y, dx, dy):
    cnt = 0
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

# BFS 시작
q = deque()
q.append((rx, ry, bx, by, 0))
visited = set()
visited.add((rx, ry, bx, by))

while q:
    rx, ry, bx, by, depth = q.popleft()
    if depth >= 10:
        break

    for i in range(4):
        nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
        nbx, nby, bcnt = move(bx, by, dx[i], dy[i])

        # 파란 구슬이 빠지면 실패
        if board[nbx][nby] == 'O':
            continue
        # 빨간 구슬만 빠지면 성공
        if board[nrx][nry] == 'O':
            print(depth + 1)
            exit()

        # 두 구슬이 겹치면, 더 많이 움직인 구슬 한 칸 뒤로
        if nrx == nbx and nry == nby:
            if rcnt > bcnt:
                nrx -= dx[i]
                nry -= dy[i]
            else:
                nbx -= dx[i]
                nby -= dy[i]

        if (nrx, nry, nbx, nby) not in visited:
            visited.add((nrx, nry, nbx, nby))
            q.append((nrx, nry, nbx, nby, depth + 1))

# 실패
print(-1)

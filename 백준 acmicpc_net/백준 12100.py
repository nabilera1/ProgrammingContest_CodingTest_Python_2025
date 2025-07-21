# https://www.acmicpc.net/problem/12100

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

max_block = 0

def move_left(b):
    new_board = []
    for row in b:
        new_row = []
        prev = None
        for val in row:
            if val == 0:
                continue
            if prev is None:
                prev = val
            elif prev == val:
                new_row.append(prev * 2)
                prev = None
            else:
                new_row.append(prev)
                prev = val
        if prev is not None:
            new_row.append(prev)
        # 0 채우기
        while len(new_row) < n:
            new_row.append(0)
        new_board.append(new_row)
    return new_board

def rotate(b):  # 시계방향 90도 회전
    return [list(reversed(col)) for col in zip(*b)]

def dfs(b, depth):
    global max_block
    if depth == 5:
        for row in b:
            max_block = max(max_block, max(row))
        return
    for _ in range(4):  # 4방향
        next_board = move_left(b)
        dfs(next_board, depth + 1)
        b = rotate(b)  # 방향 바꿔줌

dfs(board, 0)
print(max_block)

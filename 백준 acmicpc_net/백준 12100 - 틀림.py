import copy

# 입력 받기 백준 12100 "2048 (Easy)
# 일부만 동작되는 코드, 어디 부분을 수정해야하는지 생각해 보세요.
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 결과로 나올 수 있는 가장 큰 숫자를 저장하는 변수
answer = 0

# 한 줄을 왼쪽으로 밀고 합치는 함수
def merge_left(row):
    new_row = []
    prev = 0  # 전에 본 숫자
    merged = False  # 합쳐졌는지 체크
    for num in row:
        if num == 0:
            continue  # 0은 건너뛰기
        if num == prev and not merged:
            # 같은 숫자이고 아직 합쳐진 적이 없다면
            new_row[-1] = prev * 2  # 마지막 숫자와 합치기
            merged = True  # 이미 합쳐졌다고 표시
            prev = 0
        else:
            new_row.append(num)
            merged = False
            prev = num
    # 0으로 길이 맞추기
    while len(new_row) < N:
        new_row.append(0)
    return new_row

# 보드를 왼쪽으로 이동시키는 함수
def move_left(board):
    new_board = []
    for row in board:
        new_board.append(merge_left(row))
    return new_board

# 보드를 시계 방향으로 90도 회전하는 함수
def rotate_clockwise(board):
    return [list(reversed(col)) for col in zip(*board)]

# 보드를 주어진 방향으로 이동시키는 함수
# 0: 왼쪽, 1: 위, 2: 오른쪽, 3: 아래
def move(board, direction):
    new_board = copy.deepcopy(board)
    for _ in range(direction):
        new_board = rotate_clockwise(new_board)
    new_board = move_left(new_board)
    for _ in range((4 - direction) % 4):
        new_board = rotate_clockwise(new_board)
    return new_board

# 최대 5번 움직이기 - 모든 경우를 DFS로 탐색
def dfs(board, depth):
    global answer
    if depth == 5:
        for row in board:
            answer = max(answer, max(row))
        return
    for dir in range(4):  # 0: 왼쪽, 1: 위, 2: 오른쪽, 3: 아래
        moved = move(board, dir)
        if moved != board:  # 움직였을 때만 계속 탐색
            dfs(moved, depth + 1)

# 시작!
dfs(board, 0)
print(answer)


'''

3
2 2 2
4 4 4
8 8 8

'''


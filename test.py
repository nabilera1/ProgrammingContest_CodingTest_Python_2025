n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

max_block = 0

def move_left(b):
    new_board = []
    for row in b:
        new_row = []
        prev = None

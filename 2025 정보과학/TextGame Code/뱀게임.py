import os
import random
import time

W, H = 20, 10
snake = [(W//2, H//2)]
direction = (1, 0)
food = (random.randint(0, W-1), random.randint(0, H-1))

def draw():
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(H):
        for x in range(W):
            if (x, y) == food:
                print('*', end='')
            elif (x, y) in snake:
                print('O', end='')
            else:
                print('.', end='')
        print()
    print('Score:', len(snake)-1)

def move():
    global food
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    if head == food:
        snake.insert(0, head)
        food = (random.randint(0, W-1), random.randint(0, H-1))
    else:
        snake.insert(0, head)
        snake.pop()

if __name__ == '__main__':
    import msvcrt  # 윈도우용 키 입력
    while True:
        draw()
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'w': direction = (0, -1)
            if key == b's': direction = (0, 1)
            if key == b'a': direction = (-1, 0)
            if key == b'd': direction = (1, 0)
        move()
        time.sleep(0.1)
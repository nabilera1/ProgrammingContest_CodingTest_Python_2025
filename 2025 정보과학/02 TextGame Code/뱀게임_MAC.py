import curses
import random
import time
import os
import sys

W, H = 20, 10
snake = []
direction = (1, 0)
food = None

def spawn_food():
    while True:
        f = (random.randint(0, W - 1), random.randint(0, H - 1))
        if f not in snake:
            return f

def reset_game():
    global snake, direction, food
    snake = [(W // 2, H // 2)]
    direction = (1, 0)
    food = spawn_food()

def draw(stdscr):
    # 화면 클리어 후 그리기
    stdscr.clear()
    # 게임 보드
    for y in range(H):
        row = []
        for x in range(W):
            pos = (x, y)
            if pos == food:
                row.append('*')
            elif pos in snake:
                row.append('O' if pos == snake[0] else 'o')
            else:
                row.append('.')
        stdscr.addstr(y, 0, ''.join(row))
    stdscr.addstr(H + 1, 0, f"Score: {len(snake) - 1}   [WASD/Arrow] Q=quit")
    stdscr.refresh()

def move():
    global food, direction
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # 경계 래핑 (원하면 충돌로 바꿔도 됨)
    head = (head[0] % W, head[1] % H)

    # 자기 몸과 충돌 → 리셋
    if head in snake:
        reset_game()
        return

    if head == food:
        snake.insert(0, head)
        food = spawn_food()
    else:
        snake.insert(0, head)
        snake.pop()

def key_to_dir(key):
    global direction
    # 화살표
    if key == curses.KEY_UP and direction != (0, 1):
        direction = (0, -1)
    elif key == curses.KEY_DOWN and direction != (0, -1):
        direction = (0, 1)
    elif key == curses.KEY_LEFT and direction != (1, 0):
        direction = (-1, 0)
    elif key == curses.KEY_RIGHT and direction != (-1, 0):
        direction = (1, 0)
    # WASD
    elif key in (ord('w'), ord('W')) and direction != (0, 1):
        direction = (0, -1)
    elif key in (ord('s'), ord('S')) and direction != (0, -1):
        direction = (0, 1)
    elif key in (ord('a'), ord('A')) and direction != (1, 0):
        direction = (-1, 0)
    elif key in (ord('d'), ord('D')) and direction != (-1, 0):
        direction = (1, 0)

def main(stdscr):
    # curses 초기화
    curses.curs_set(0)        # 커서 숨기기
    stdscr.nodelay(True)      # non-blocking 입력
    stdscr.keypad(True)       # 화살표 인식
    reset_game()

    last_tick = time.time()
    TICK = 0.08  # 게임 틱 간격

    while True:
        # 입력 처리
        try:
            key = stdscr.getch()
        except curses.error:
            key = -1
        if key != -1:
            if key in (ord('q'), ord('Q')):
                return
            key_to_dir(key)

        # 틱마다 이동
        now = time.time()
        if now - last_tick >= TICK:
            move()
            last_tick = now

        draw(stdscr)
        time.sleep(0.01)

if __name__ == "__main__":
    # PyCharm 기본 콘솔은 TTY가 아닐 수 있음 → 안내
    if not sys.stdin.isatty() or not sys.stdout.isatty():
        print("현재 콘솔이 TTY가 아닙니다. 다음 중 하나로 실행하세요:")
        print("  1) PyCharm 설정에서 Run/Debug → 'Emulate terminal in output console' 활성화")
        print("  2) macOS Terminal에서: python 뱀게임_MAC.py")
        # 그래도 시도하고 싶다면 주석을 해제하세요
        # sys.exit(1)

    curses.wrapper(main)



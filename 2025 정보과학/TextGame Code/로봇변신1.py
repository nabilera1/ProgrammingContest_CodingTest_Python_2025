# ascii_transformer.py
import os
import time
import sys

CLEAR = 'cls' if os.name == 'nt' else 'clear'

def cls():
    os.system(CLEAR)

def draw(frame: str, title: str = ""):
    cls()
    if title:
        print(f"[ {title} ]")
    print(frame)

def animate(frames, title="", delay=0.12, repeat=1):
    for _ in range(repeat):
        for f in frames:
            draw(f, title)
            time.sleep(delay)

# ====== ASCII FRAMES ======
ROBOT_IDLE = r"""
      __
     /__\     ___
   _|    |___/___\___
  /_|____|___|_|_|__\
    /  \/  \  | |
   /__/ /\ \_\| |
      /_/  \_\  |
      (  ||  )  |
       \_||_/  / \
        /  \  /___\
       /____\  | |
        |  |   | |
"""

ROBOT_WALK1 = r"""
      __
     /__\     ___
   _|    |___/___\___
  /_|____|___|_|_|__\
    /  \/  \  | |
   /__/ /\ \_\| |
      /_/  \_\  |
     _(  ||  )_ |
    /  \||_/  \|
   /____\/\____\
      _|_  | |
       |    | |
"""

ROBOT_WALK2 = r"""
      __
     /__\     ___
   _|    |___/___\___
  /_|____|___|_|_|__\
    /  \/  \  | |
   /__/ /\ \_\| |
      /_/  \_\  |
      (  ||  )  |
     / \||_/ \  |
   _/___\  /___\_
      | |  | |
      | |  | |
"""

CAR_IDLE = r"""
       ______________________
   ___/______________________\___
  / _|_|  _  _  _  _  _  _  |_|_ \
 | /  _  / \/ \/ \/ \/ \/ \   _ \ |
 |_| |_|_|__|__|__|__|__|_|_|_| |_|
   O                         O
"""

CAR_DRIVE1 = r"""
       ______________________
   ___/______________________\___
  / _|_|  _  _  _  _  _  _  |_|_ \
 | /  _  / \/ \/ \/ \/ \/ \   _ \ |
 |_| |_|_|__|__|__|__|__|_|_|_| |_|
    O                         O
"""

CAR_DRIVE2 = r"""
       ______________________
   ___/______________________\___
  / _|_|  _  _  _  _  _  _  |_|_ \
 | /  _  / \/ \/ \/ \/ \/ \   _ \ |
 |_| |_|_|__|__|__|__|__|_|_|_| |_|
 O                           O
"""

# 변신 중간 프레임(간단한 변형 연출)
TRANS_1 = r"""
      __
     /__\     ___
   _|    |___/___\___
  /_|____|___|_|_|__\
     \      /  | |
      \____/   | |
       |  |    | |
       |__|   /___\
        /\     | |
       /__\    | |
"""

TRANS_2 = r"""
       ______________
    __/______________\__
   / _  _  _  _  _  _  _\
  |  \_/_\_/_\_/_\_/_\_/ |
  |______________________|
     \              /
      \____________/
       O          O
"""

# 시퀀스
ROBOT_WALK_SEQ = [ROBOT_WALK1, ROBOT_WALK2]
CAR_DRIVE_SEQ = [CAR_DRIVE1, CAR_DRIVE2]
TO_CAR_SEQ = [ROBOT_IDLE, TRANS_1, TRANS_2, CAR_IDLE]
TO_ROBOT_SEQ = [CAR_IDLE, TRANS_2, TRANS_1, ROBOT_IDLE]

def main():
    speed = 0.12  # 기본 애니메이션 속도(초)
    mode = "robot"  # 시작 상태

    cls()
    print("🤖 ASCII Transformer")
    print("- 명령: robot, walk, car, drive, transform, clear, speed 0.05, exit")
    print("- 팁: 고정폭(모노스페이스) 글꼴을 사용하면 정렬이 예쁩니다.\n")
    time.sleep(1.2)

    # 시작 화면
    draw(ROBOT_IDLE, "Robot: Idle")

    while True:
        try:
            cmd = input("\n> 명령 입력: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\n종료합니다.")
            return

        if not cmd:
            continue

        if cmd == "exit" or cmd == "quit":
            print("종료합니다. 안녕히 계세요!")
            return

        if cmd == "clear":
            cls()
            continue

        if cmd.startswith("speed"):
            parts = cmd.split()
            if len(parts) == 2:
                try:
                    speed = max(0.02, float(parts[1]))
                    print(f"속도 변경: {speed:.2f}초/프레임 (작을수록 빠름)")
                except ValueError:
                    print("예: speed 0.08")
            else:
                print("예: speed 0.08")
            continue

        if cmd == "robot":
            mode = "robot"
            draw(ROBOT_IDLE, "Robot: Idle")
            continue

        if cmd == "car":
            mode = "car"
            draw(CAR_IDLE, "Car: Idle")
            continue

        if cmd == "walk":
            mode = "robot"
            animate(ROBOT_WALK_SEQ, "Robot: Walking", delay=speed, repeat=6)
            draw(ROBOT_IDLE, "Robot: Idle")
            continue

        if cmd == "drive":
            mode = "car"
            animate(CAR_DRIVE_SEQ, "Car: Driving", delay=speed, repeat=8)
            draw(CAR_IDLE, "Car: Idle")
            continue

        if cmd == "transform":
            if mode == "robot":
                animate(TO_CAR_SEQ, "Transforming: Robot → Car", delay=speed, repeat=1)
                mode = "car"
                draw(CAR_IDLE, "Car: Idle")
            else:
                animate(TO_ROBOT_SEQ, "Transforming: Car → Robot", delay=speed, repeat=1)
                mode = "robot"
                draw(ROBOT_IDLE, "Robot: Idle")
            continue

        # 알 수 없는 명령
        print("알 수 없는 명령입니다. 사용 가능한 명령: robot, walk, car, drive, transform, clear, speed 0.05, exit")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # 콘솔 환경에 따른 예외가 나와도 종료 메시지를 남기고 종료
        print(f"\n오류가 발생하여 종료합니다: {e}", file=sys.stderr)

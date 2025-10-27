# simple_transformer.py
import os
import time

CLEAR = 'cls' if os.name == 'nt' else 'clear'

def cls():
    os.system(CLEAR)

def show(frame, title=""):
    cls()
    print(f"[ {title} ]\n")
    print(frame)

def animate(frames, title="", delay=0.2):
    for f in frames:
        show(f, title)
        time.sleep(delay)

# ====== 간단한 ASCII 아트 ======
ROBOT = r"""
   [🤖]
    /|\
    / \
"""

ROBOT_MOVE1 = r"""
   [🤖]
   _/|_
    / \
"""

ROBOT_MOVE2 = r"""
   [🤖]
    \|/
   _/ \
"""

CAR = r"""
 _______
| 🚗   |
|_______|
   O   O
"""

CAR_MOVE1 = r"""
 _______
| 🚗== |
|_______|
   O   O
"""

CAR_MOVE2 = r"""
 _______
| ==🚗 |
|_______|
   O   O
"""

TRANS1 = r"""
   [🤖]
    /|
   _/
"""

TRANS2 = r"""
  __🤖__
 /_____\
  \___/
   O O
"""

# 시퀀스 정의
ROBOT_WALK = [ROBOT_MOVE1, ROBOT_MOVE2]
CAR_DRIVE = [CAR_MOVE1, CAR_MOVE2]
TO_CAR = [ROBOT, TRANS1, TRANS2, CAR]
TO_ROBOT = [CAR, TRANS2, TRANS1, ROBOT]

def main():
    mode = "robot"

    while True:
        cls()
        print("🤖 TRANSFORMER ANIMATION\n")
        print("1. 로봇 모드")
        print("2. 자동차 모드")
        print("3. 변신")
        print("4. 종료\n")

        choice = input("입력> ").strip()

        if choice == "1":
            animate(ROBOT_WALK, "로봇 이동 중", delay=0.25)
            show(ROBOT, "로봇 대기")
            input("\n(Enter 키로 계속)")
        elif choice == "2":
            animate(CAR_DRIVE, "자동차 주행 중", delay=0.25)
            show(CAR, "자동차 대기")
            input("\n(Enter 키로 계속)")
        elif choice == "3":
            if mode == "robot":
                animate(TO_CAR, "로봇 → 자동차 변신", delay=0.25)
                mode = "car"
            else:
                animate(TO_ROBOT, "자동차 → 로봇 변신", delay=0.25)
                mode = "robot"
            input("\n(Enter 키로 계속)")
        elif choice == "4":
            cls()
            print("시스템 종료.")
            break
        else:
            print("잘못된 입력입니다.")
            time.sleep(1)

if __name__ == "__main__":
    main()

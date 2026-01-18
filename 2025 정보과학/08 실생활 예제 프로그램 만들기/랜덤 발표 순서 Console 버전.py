'''
GUI 라이브러리(Tkinter 등) 없이 오직 텍스트(Console) 환경에서 작동하는 버전입니다.
파이참의 하단 '실행(Run)' 창에서 바로 결과를 확인할 수 있습니다.

화면을 지우거나 새로 그리는 대신, 커서를 줄의 맨 앞으로 되돌리는 캐리지 리턴(\r) 기능을
사용하여 숫자가 다다닥 바뀌는 슬롯머신 효과를 텍스트로 구현했습니다.

핵심 기술 (\r 캐리지 리턴):

print 함수는 기본적으로 줄을 바꿉니다.
하지만 애니메이션 효과를 내려면 같은 줄에서 글자만 바뀌어야 합니다.

\r 문자를 문자열 앞에 넣으면 커서가 줄의 맨 앞으로 이동합니다.
그 상태에서 다시 글자를 쓰면 이전 글자가 덮어씌워지면서 마치 숫자가 움직이는 것처럼 보입니다.

디자인:

이모티콘을 제외하고 대괄호 [ ]와 등호 = 등을 사용하여
깔끔한 CLI(Command Line Interface) 스타일을 연출했습니다.
'''

import time
import random
import sys


def main():
    # 1부터 14까지의 숫자를 리스트로 생성
    numbers = list(range(1, 15))

    # 공정한 추첨을 위해 리스트를 무작위로 섞음
    random.shuffle(numbers)

    # 타이틀 출력
    print("\n")
    print("========================================")
    print("        PRESENTATION ORDER DRAW         ")
    print("========================================")
    print("   Determining the order for 14 people  ")
    print("========================================")
    time.sleep(1)  # 잠시 대기

    print("\nStarting the draw...\n")
    time.sleep(1)

    # 1번째 순서부터 14번째 순서까지 반복
    for i, final_num in enumerate(numbers):
        rank = i + 1

        # 긴장감을 주는 롤링 애니메이션 효과 (약 1.5초간 지속)
        # 30번 빠르게 숫자를 바꿔서 보여줌
        for _ in range(30):
            # 1~14 사이의 임의의 숫자를 생성 (보여주기용 가짜 숫자)
            temp_num = random.randint(1, 14)

            # \r은 커서를 해당 줄의 맨 앞으로 이동시킴 (줄바꿈 없이 덮어쓰기)
            # end=''는 print 함수가 자동으로 줄바꿈을 하지 않도록 설정
            sys.stdout.write(f"\r  [Processing] Rank {rank:02d} ... {temp_num:02d}  ")
            sys.stdout.flush()  # 버퍼를 비워 화면에 즉시 출력
            time.sleep(0.05)  # 0.05초 대기 (숫자가 바뀌는 속도)

        # 최종 확정 번호 출력
        # 마지막에는 줄바꿈(\n)을 포함하여 확정된 상태로 고정
        sys.stdout.write(f"\r  [ CONFIRMED ] Rank {rank:02d} >>> [ {final_num:02d} ]    \n")
        sys.stdout.flush()

        # 다음 순서 공개 전 잠깐의 뜸들이기 (긴장감 조성)
        time.sleep(0.8)

    # 마무리 멘트
    print("\n========================================")
    print("             DRAW COMPLETED             ")
    print("========================================")

    # 프로그램이 바로 꺼지는 것을 방지 (터미널 환경에 따라 필요할 수 있음)
    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()

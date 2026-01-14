import time
import random
import sys

# ── 공용: 초간단 프로그레스바(보기만, 로직 영향 없음)
def progress_bar(duration=1.2, label="준비"):
    steps = 20
    print(label, end=" ")
    for i in range(steps + 1):
        filled = "█" * i
        empty = "-" * (steps - i)
        pct = int(i / steps * 100)
        print(f"\r{label}: [{filled}{empty}] {pct:3d}%", end="")
        time.sleep(duration / steps)
    print()  # 줄바꿈

# 1) 반응속도 게임
def game_reflex():
    print("\n=== 반응속도 게임 ===")
    print("곧 '지금!'이 뜨면 즉시 엔터를 누르세요.")
    time.sleep(random.uniform(1.5, 4.0))  # 랜덤 대기
    print("지금!")
    start = time.time()
    input()  # 엔터 대기, 미리 엔터치면 되는 문제 발생
    elapsed = time.time() - start
    print(f"반응 시간: {elapsed:.3f}초")
    if elapsed < 0.20:
        print("번개 반사신경!")
    elif elapsed < 0.35:
        print("훌륭해요!")
    elif elapsed < 0.50:
        print("나쁘지 않아요.")
    else:
        print("다음엔 더 빨리!")

# 2) 폭탄 해제 타자 챌린지
def game_typing():
    print("\n=== 폭탄 해제 챌린지 ===")
    WORDS = ["python", "school", "ramen", "puzzle", "dragon", "cookie", "matrix"]
    target = random.choice(WORDS)
    limit = 5  # 제한시간(초)
    print(f"제한시간 {limit}초 안에 아래 단어를 정확히 입력하세요.")
    print("단어:", target)
    start = time.time()
    typed = input("> ").strip()
    elapsed = time.time() - start
    print(f"입력 시간: {elapsed:.2f}초")
    if elapsed <= limit and typed == target:
        print("성공! 폭탄 해제 완료!")
    elif typed != target:
        print("오타! 폭탄이 터졌습니다…")
    else:
        print("시간 초과! 폭탄이 터졌습니다…")

def main():
    while True:
        print("\n===== 타임 미니게임 =====")
        print("1) 반응속도 게임")
        print("2) 폭탄 해제 타자 챌린지")
        print("3) 종료")
        choice = input("번호 선택: ").strip()

        if choice == "1":
            progress_bar(0.8, "준비 중")
            game_reflex()
        elif choice == "2":
            progress_bar(0.8, "장전 중")
            game_typing()
        elif choice == "3":
            print("안녕!")
            break
        else:
            print("올바른 번호를 입력하세요!")

if __name__ == "__main__":
    main()

import time
import random

WORDS = ["python", "school", "ramen", "puzzle", "dragon", "cookie", "matrix"]

print("=== 폭탄 해제 챌린지 ===")
target = random.choice(WORDS)
limit = 5  # 제한시간(초)

print(f"제한시간 {limit}초 안에 아래 단어를 정확히 입력하세요.")
print("단어:", target)

start = time.time()
typed = input("> ").strip()
elapsed = time.time() - start

print(f"입력 시간: {elapsed:.2f}초")
if elapsed <= limit and typed == target:
    print("성공! 폭탄이 해제되었습니다!")
elif typed != target:
    print("오타! 폭탄이 터졌습니다...")
else:
    print("시간 초과! 폭탄이 터졌습니채다...")
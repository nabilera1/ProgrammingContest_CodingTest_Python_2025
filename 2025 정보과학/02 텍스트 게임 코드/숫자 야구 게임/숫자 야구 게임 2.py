import random

# 1. 게임 설정
secret_numbers = random.sample("0123456789", 3)
max_attempts = 10  # 최대 시도 횟수 설정
try_count = 0  # 현재 시도 횟수

print(f" 숫자 야구 게임 (HARD MODE) ")
print(f"기회는 총 {max_attempts}번입니다. 신중하게 맞춰보세요!")
print("-" * 40)

# 2. 게임 루프
while True:
    try_count += 1
    remaining_attempts = max_attempts - try_count  # 남은 횟수 계산

    # 사용자 입력
    print(f"\n[시도 {try_count}/{max_attempts}] 숫자 3개를 입력하세요 (남은 기회: {remaining_attempts}번)")
    user_input = input("입력 > ").strip()

    # --- 입력값 검증 ---
    if len(user_input) != 3:
        print(" 3자리 숫자를 입력해야 합니다. (횟수는 차감되지 않습니다)")
        try_count -= 1  # 유효하지 않은 입력이므로 횟수 복구
        continue
    if not user_input.isdigit():
        print(" 숫자만 입력해주세요.")
        try_count -= 1
        continue
    if len(set(user_input)) != 3:
        print(" 중복되는 숫자가 있습니다.")
        try_count -= 1
        continue

    # --- 판정 로직 ---
    strikes = 0
    balls = 0

    for i, num in enumerate(user_input):
        if num == secret_numbers[i]:
            strikes += 1
        elif num in secret_numbers:
            balls += 1

    # --- 결과 출력 ---
    print(f" 결과: {strikes} 스트라이크, {balls} 볼")

    # --- [승리] 3 스트라이크면 게임 종료 ---
    if strikes == 3:
        print("\n" + "=" * 40)
        print(f" 축하합니다! {try_count}번 만에 홈런을 쳤습니다! ")
        print("=" * 40)
        break

    # --- [패배] 기회를 모두 소진했는지 확인 ---
    if try_count >= max_attempts:
        print("\n" + "=" * 40)
        print(" GAME OVER! 모든 기회를 소진했습니다.")
        print(f"정답은 [{' '.join(secret_numbers)}] 였습니다.")
        print("=" * 40)
        break
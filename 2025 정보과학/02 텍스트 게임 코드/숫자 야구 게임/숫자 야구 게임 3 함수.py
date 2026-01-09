import random


def generate_numbers():
    """0~9 사이의 중복되지 않는 숫자 3개 생성"""
    numbers = list(range(10))
    random.shuffle(numbers)
    return numbers[:3]


def get_strike_ball(target, guess):
    """스트라이크와 볼 판정"""
    strike = 0
    ball = 0

    for i in range(3):
        if guess[i] == target[i]:
            strike += 1
        elif guess[i] in target:
            ball += 1

    return strike, ball


def play_numeric_baseball():
    print("⚾ [숫자 야구 게임]을 시작합니다! ⚾")
    print("0~9 사이의 서로 다른 숫자 3개를 맞춰보세요.")

    target_numbers = generate_numbers()
    attempts = 0

    while True:
        try:
            user_input = input(f"\n[{attempts + 1}회차] 숫자 3개를 입력하세요 (예: 123) > ")

            # 입력 검증
            if not user_input.isdigit() or len(user_input) != 3:
                print("⚠️ 오류: 3자리의 숫자를 입력해주세요.")
                continue

            # 입력값을 숫자 리스트로 변환
            guess_numbers = [int(digit) for digit in user_input]

            # 중복 입력 확인
            if len(set(guess_numbers)) != 3:
                print("⚠️ 오류: 중복된 숫자가 있습니다.")
                continue

            attempts += 1
            strike, ball = get_strike_ball(target_numbers, guess_numbers)

            if strike == 3:
                print(f"\n🎉 정답입니다! {attempts}번 만에 맞추셨습니다!")
                print(f"정답 숫자: {target_numbers}")
                break
            else:
                print(f"👉 결과: {strike} 스트라이크, {ball} 볼")

        except ValueError:
            print("⚠️ 오류: 올바른 값을 입력해주세요.")


if __name__ == "__main__":
    play_numeric_baseball()
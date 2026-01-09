import random

options = ["가위", "바위", "보"]

while True:
    print("\n--- 가위바위보 게임 ---")
    user = input("가위/바위/보 입력 (종료하려면 '그만'): ")

    if user == "그만":
        print("게임을 종료합니다.")
        break  # 반복문 탈출

    if user not in options:
        print("잘못된 입력입니다. 다시 입력해주세요.")
        continue  # 다시 처음으로 돌아감

    computer = random.choice(options)
    print(f"💻 컴퓨터: {computer}")

    if user == computer:
        print("비겼습니다!")
    elif (user == "가위" and computer == "보") or \
         (user == "바위" and computer == "가위") or \
         (user == "보" and computer == "바위"):
        print("이겼습니다! 승리!")
    else:
        print("졌습니다.. 다음 기회에!")
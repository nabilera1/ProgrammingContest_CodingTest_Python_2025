import random

# 1. 가위바위보 재료 준비
options = ["가위", "바위", "보"]
computer = random.choice(options)  # 컴퓨터가 랜덤으로 선택

# 2. 사용자 입력 받기
user = input("가위, 바위, 보 중 하나를 입력하세요: ")

print(f"나: {user}, 컴퓨터: {computer}")

# 3. 승패 판정 (핵심 로직)
if user == computer:
    print("비겼습니다! 😐")
elif (user == "가위" and computer == "보") or \
     (user == "바위" and computer == "가위") or \
     (user == "보" and computer == "바위"):
    print("이겼습니다! 🎉")
else:
    print("졌습니다... 😭")
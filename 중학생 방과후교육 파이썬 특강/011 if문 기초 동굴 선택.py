

# lv 1

import random
print("동굴 입구에서 왼쪽/오른쪽?")
c=input("L/R: ").strip().upper()
if c=="L":
    print("보물 발견! +100골드")
else:
    if random.randint(0,1):
        print("동굴에서 마법사를 만났다.")
    else:
        print("함정에 걸렸다! 게임오버")


# lv 2

import random
print("동굴 입구에서 왼쪽/오른쪽?")
c = input("L/R: ").strip().upper()[:1]   # 앞뒤 공백 제거 + 첫 글자만 사용
if c == "L":
    print("보물 발견! +100골드")
elif c == "R":
    if random.randint(0, 1):
        print("동굴에서 마법사를 만났다.")
    else:
        print("함정! 게임오버")
else:
    print("유효한 입력이 아닙니다. (L 또는 R)")


# lv 3
# 안전한 입력 처리 + 재도전 기능
import random

def choose_lr():
    while True:
        c = input("L/R: ").strip().upper()[:1]  # 공백 제거, 첫 글자만
        if c in ("L", "R"):
            return c
        print("L 또는 R만 입력해주세요!")

def play():
    print("동굴 입구에서 왼쪽/오른쪽?")
    c = choose_lr()
    if c == "L":
        print("보물 발견! +100골드")
        return "win" # 결과 문자열은 이후 확장 포인트
    # 오른쪽을 고른 경우: 무작위 사건
    if random.randint(0, 1):
        print("동굴에서 마법사를 만났다. 축복을 받았다!")
        return "bless"
    else:
        print("함정에 걸렸다! 게임오버")
        return "lose"

if __name__ == "__main__":
    while True:
        result = play()  # 결과 문자열은 이후 확장 포인트
        again = input("다시 할까요? (Y/N): ").strip().lower()
        if not again.startswith("y"):
            print("플레이해줘서 고마워요!"); break




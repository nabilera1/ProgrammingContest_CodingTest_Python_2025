import random

# 1부터 50 사이의 숫자 하나를 랜덤으로 뽑음
secret = random.randint(1, 50)

print("1부터 50 사이의 숫자를 맞춰보세요!")
print("기회는 5번 있습니다.")

# 5번 시도
for chance in range(1, 6):
    guess = int(input(f"{chance}번째 도전 >> "))

    if guess == secret:
        print("정답입니다!")
        break
    elif guess < secret:
        print("더 큰 수예요!")
    else:
        print("더 작은 수예요!")

# 다 틀렸을 때
else:
    print("아쉽습니다. 정답은", secret, "이었습니다.")

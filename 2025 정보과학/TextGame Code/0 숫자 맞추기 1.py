import random

secret = random.randint(1, 10)  # 1~10 사이
guess = int(input('1~10 숫자를 한 번만 맞춰보세요: '))

print('정답입니다!' if guess == secret else f'아쉽습니다! 정답은 {secret}')

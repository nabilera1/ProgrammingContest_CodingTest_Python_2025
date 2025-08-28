import random

# 조건문·반복문·리스트·문자열 학습하기
HANGMAN = [
'''
  +---+
  |   |
      |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========='''
]


# 단어 목록
words = ["apple", "banana", "grape", "orange", "melon"]
secret = random.choice(words)  # 랜덤 선택

missed = ""
correct = ""

print("H A N G M A N")

while True:
    # 그림 출력
    print(HANGMAN[len(missed)])

    # 현재 상태 출력
    display = ""
    for ch in secret:
        display += ch if ch in correct else "_"
    print("단어:", " ".join(display))
    print("틀린 글자:", " ".join(missed))

    # 종료 조건
    if display == secret:
        print("축하합니다! 정답은", secret)
        break
    if len(missed) == len(HANGMAN) - 1:
        print("실패! 정답은", secret)
        break

    # 사용자 입력
    guess = input("글자를 입력하세요: ").lower()
    if guess in secret:
        correct += guess
    else:
        missed += guess

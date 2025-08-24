import random

# 0~6까지 총 7단계 그림
HANGMANPICS = [
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
words = "apple banana grape orange peach strawberry watermelon".split()

# 단어 하나를 무작위로 뽑는 함수
def get_random_word(word_list):
    return random.choice(word_list)

# 현재 게임 상태를 화면에 출력하는 함수
def display_game(missed_letters, correct_letters, secret_word):
    print(HANGMANPICS[len(missed_letters)])   # 틀린 횟수에 따라 그림 출력
    print()

    # 틀린 글자 보여주기
    print("틀린 글자:", end=" ")
    for letter in missed_letters:
        print(letter, end=" ")
    print("\n")

    # 단어의 맞춘 글자와 안 맞춘 글자를 구분해서 출력
    blanks = "_" * len(secret_word)   # 처음엔 전부 빈칸
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
    for letter in blanks:
        print(letter, end=" ")
    print("\n")

# 플레이어가 입력한 글자가 올바른 입력인지 확인하는 함수
def get_guess(already_guessed):
    while True:
        guess = input("알파벳 한 글자를 입력하세요: ").lower()
        if len(guess) != 1:
            print("한 글자만 입력해야 합니다.")
        elif guess in already_guessed:
            print("이미 입력한 글자입니다. 다른 글자를 고르세요.")
        elif not guess.isalpha():
            print("알파벳만 입력할 수 있습니다.")
        else:
            return guess

# 다시 게임할지 묻는 함수
def play_again():
    return input("다시 게임하시겠습니까? (yes or no): ").lower().startswith("y")

# -------------------------------
# 메인 게임 루프
# -------------------------------
print("H A N G M A N 게임에 오신 것을 환영합니다!")

missed_letters = ""   # 틀린 글자 저장
correct_letters = ""  # 맞춘 글자 저장
secret_word = get_random_word(words)   # 숨겨진 단어
game_is_done = False

while True:
    display_game(missed_letters, correct_letters, secret_word)

    # 플레이어 입력 받기
    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word:   # 맞췄을 경우
        correct_letters += guess

        # 모든 글자를 다 맞췄는지 확인
        found_all_letters = True
        for letter in secret_word:
            if letter not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print(f"축하합니다! 단어 '{secret_word}' 를 모두 맞추셨습니다!")
            game_is_done = True
    else:   # 틀렸을 경우
        missed_letters += guess

        if len(missed_letters) == len(HANGMANPICS) - 1:
            display_game(missed_letters, correct_letters, secret_word)
            print("틀린 글자를 너무 많이 입력했습니다!")
            print(f"정답은 '{secret_word}' 였습니다.")
            game_is_done = True

    # 게임 끝났을 때 다시 시작 여부 확인
    if game_is_done:
        if play_again():
            missed_letters = ""
            correct_letters = ""
            game_is_done = False
            secret_word = get_random_word(words)
        else:
            break

# hangman_level1_fileio.py
import random
import sys
from datetime import datetime


WORDS_PATH = "words_easy.txt"
LOG_PATH = "hangman_log.csv"


DEFAULT_WORDS = ["apple", "banana", "grape", "orange", "melon"]


HANGMANPICS = [
r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]


def ensure_word_file(path: str, defaults: list[str]) -> None:
    try:
        with open(path, "r", encoding="utf-8") as f:
            _ = f.read(1)
    except FileNotFoundError:
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(defaults))
        print(f"[알림] '{path}'가 없어 기본 단어 파일을 생성함.")


def load_words(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        words = [line.strip().lower() for line in f if line.strip()]
    words = sorted(set(words))
    if not words:
        raise ValueError(f"'{path}'에 유효한 단어가 없음")
    return words


def log_result(secret: str, win: bool, tried: list[str]) -> None:
    header_needed = False
    try:
        with open(LOG_PATH, "r", encoding="utf-8") as _:
            pass
    except FileNotFoundError:
        header_needed = True
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        if header_needed:
            f.write("time,level,secret,win,tried\n")
        f.write(f"{datetime.now().isoformat(timespec='seconds')},1,{secret},{int(win)},{''.join(tried)}\n")


def display_state(pics, secret, correct, missed):
    print(pics[len(missed)])
    shown = " ".join([ch if ch in correct else "_" for ch in secret])
    print("\n단어:", shown)
    if missed:
        print("틀린 글자:", " ".join(sorted(missed)))
    print()


def get_guess(already: set[str]) -> str:
    while True:
        g = input("알파벳 한 글자 입력: ").strip().lower()
        if len(g) != 1 or not g.isalpha():
            print("한 글자의 알파벳만 입력.")
            continue
        if g in already:
            print("이미 시도한 글자.")
            continue
        return g


def is_won(secret: str, correct: set[str]) -> bool:
    return all(ch in correct for ch in secret)


def play_level1():
    ensure_word_file(WORDS_PATH, DEFAULT_WORDS)
    words = load_words(WORDS_PATH)
    secret = random.choice(words)


    missed, correct = set(), set()
    tried_order = []
    max_misses = len(HANGMANPICS) - 1


    print("H A N G M A N  - Level 1 (파일 입출력)")


    while True:
        display_state(HANGMANPICS, secret, correct, missed)


        if is_won(secret, correct):
            print(f"정답! 단어는 '{secret}'")
            log_result(secret, True, tried_order)
            break


        if len(missed) >= max_misses:
            print(HANGMANPICS[-1])
            print(f"실패! 정답은 '{secret}'")
            log_result(secret, False, tried_order)
            break


        guess = get_guess(missed | correct)
        tried_order.append(guess)
        if guess in secret:
            print(f"맞음: '{guess}'")
            correct.add(guess)
        else:
            print(f"틀림: '{guess}'")
            missed.add(guess)


def main():
    while True:
        try:
            play_level1()
        except (FileNotFoundError, ValueError) as e:
            print("[오류]", e)
        again = input("\n다시 하기? (y/n): ").strip().lower()
        if again != "y":
            print("끝!")
            sys.exit(0)


if __name__ == "__main__":
    main()

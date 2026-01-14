# ============================================================
#  폭탄 해제 챌린지: 업그레이드 (with 실시간 프로그레스바)
#  - 레벨 선택(Easy/Normal/Hard)
#  - 제한시간 동안 입력 대기 + 진행률 바 애니메이션
#  - 라이프 3개, 콤보/최고기록, 라운드 진행
#  - 표준 라이브러리만 사용: time, random, threading, queue, sys
# ============================================================

import time
import random
import sys
import threading
import queue

# ---------- 유틸: 출력/애니메이션 ----------
def print_bar(ratio, width=24, label="타이머"):
    ratio = max(0.0, min(1.0, ratio))
    filled = int(width * ratio)
    bar = "█" * filled + "-" * (width - filled)
    pct = int(ratio * 100)
    sys.stdout.write(f"\r{label}: [{bar}] {pct:3d}% ")
    sys.stdout.flush()

def slowprint(s, delay=0.02):
    for ch in s:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def clear_line():
    sys.stdout.write("\r" + " " * 80 + "\r")
    sys.stdout.flush()

# ---------- 입력: 제한시간 내 실시간 프로그레스바 ----------
def timed_input(prompt, limit_sec, tick=0.05, label="타이머"):
    """
    제한시간 동안 입력을 받는다(엔터로 확정).
    - 입력 중에도 실시간 프로그레스바가 화면에 그려짐.
    - 시간 내 입력하면 (text, elapsed) 반환
    - 시간 초과면 (None, limit_sec) 반환
    """
    q = queue.Queue()

    def _reader():
        try:
            text = input(prompt)
            q.put(text)
        except EOFError:
            q.put("")

    t = threading.Thread(target=_reader, daemon=True)
    t.start()

    start = time.time()
    end_time = start + limit_sec
    # 진행률 바: 0% -> 100%
    while time.time() < end_time:
        if not q.empty():
            clear_line()
            text = q.get()
            elapsed = time.time() - start
            return text, elapsed
        ratio = (time.time() - start) / limit_sec
        print_bar(ratio, label=label)
        time.sleep(tick)

    # 시간 초과
    clear_line()
    # 남아있던 입력 버퍼 비우기(있으면)
    if not q.empty():
        _ = q.get()
    return None, limit_sec

# ---------- 게임 데이터 ----------
WORDS_EZ = [
    "apple", "piano", "robot", "cookie", "school",
    "matrix", "dragon", "teacher", "puzzle", "solar"
]
WORDS_NM = [
    "variable", "function", "notebook", "language", "dungeon",
    "mystery", "gravity", "network", "quantum", "spiral"
]
WORDS_HD = [
    "synchronization", "characteristic", "extraordinary", "acknowledgment",
    "configuration", "miscommunication", "implementation", "intermediate",
    "responsibility", "deconstruction"
]

LEVELS = {
    "1": ("Easy",   7.0, WORDS_EZ),
    "2": ("Normal", 5.0, WORDS_NM),
    "3": ("Hard",   3.5, WORDS_HD),
}

# 가끔 뜨는 랜덤 효과(라운드 시작 시 20% 확률)
RANDOM_EVENTS = [
    ("+0.8초 보너스! 여유가 생겼다.", +0.8),
    ("-0.7초 페널티! 긴장하세요.", -0.7),
    ("점수 +30 보너스!", "score:+30"),
    ("이번 라운드는 대문자/소문자 구분!", "case:on"),
]

# ---------- 점수 계산 ----------
def calc_points(limit, elapsed, correct, base=100):
    """
    시간 여유가 많을수록 점수 가산. 틀리면 0점.
    """
    if not correct:
        return 0
    # 남은 시간 비율(0~1)을 점수로 환산
    remain = max(0.0, limit - elapsed)
    ratio = remain / limit  # 0.0 ~ 1.0
    return base + int(80 * ratio)

# ---------- 메인 게임 ----------
def play_round(target, limit, case_sensitive=False):
    print(f"\n단어(제한 {limit:.1f}초): {target}")
    if not case_sensitive:
        print("(대소문자 구분 없음)")

    user, elapsed = timed_input("> ", limit, label="카운트다운")
    # 판정
    if user is None:
        print("시간 초과!")
        return False, elapsed, 0

    if case_sensitive:
        ok = (user == target)
    else:
        ok = (user.strip().lower() == target.lower())

    if ok:
        print(f"정답! ({elapsed:.2f}초)")
        pts = calc_points(limit, elapsed, True)
        return True, elapsed, pts
    else:
        print(f"오답! 정답은 '{target}'")
        return False, elapsed, 0

def game():
    slowprint("=== 폭탄 해제 챌린지: 업그레이드 ===", 0.01)
    print("레벨을 선택하세요:")
    print("  1) Easy   (제한 7.0초, 쉬운 단어)")
    print("  2) Normal (제한 5.0초, 중간 단어)")
    print("  3) Hard   (제한 3.5초, 어려운 단어)")

    level_key = input("번호: ").strip()
    if level_key not in LEVELS:
        level_key = "2"
        print("기본값 Normal로 진행합니다.")
    level_name, base_limit, words = LEVELS[level_key]

    lives = 3
    score = 0
    best_time = None
    combo = 0
    round_no = 0

    slowprint(f"\n[{level_name}] 모드 시작! 라이프 {lives}개 행운을 빕니다!", 0.01)

    while lives > 0:
        round_no += 1
        print(f"\n----- Round {round_no} -----")
        target = random.choice(words)

        # 라운덤 이벤트(20% 확률)
        limit = base_limit
        case_sensitive = False
        if random.random() < 0.20:
            event = random.choice(RANDOM_EVENTS)
            msg, eff = event
            print(msg)
            if isinstance(eff, (int, float)):
                limit = max(1.5, base_limit + eff)
            elif eff == "case:on":
                case_sensitive = True
            elif eff.startswith("score:"):
                add = int(eff.split(":")[1])
                score += add
                print(f"(즉시 점수 +{add})")

        # 라운드 플레이
        ok, elapsed, pts = play_round(target, limit, case_sensitive)

        if ok:
            score += pts
            combo += 1
            best_time = elapsed if (best_time is None or elapsed < best_time) else best_time
            print(f"점수 +{pts} | 누적 {score}점 | 콤보 {combo}")
            # 콤보 보너스
            if combo > 0 and combo % 3 == 0:
                bonus = 25
                score += bonus
                print(f"🔥 콤보 {combo}! 보너스 +{bonus} (누적 {score})")
        else:
            lives -= 1
            combo = 0
            print(f"남은 라이프: {lives}")

        # 선택지: 계속/그만
        if lives > 0:
            cmd = input("계속하려면 Enter, 그만하려면 q: ").strip().lower()
            if cmd == "q":
                break

    # 결과 요약
    print("\n===== 결과 =====")
    print(f"- 모드: {level_name}")
    print(f"- 총점: {score}점")
    print(f"- 최고 반응: {best_time:.2f}초" if best_time is not None else "- 최고 반응: 기록 없음")
    if score >= 350:
        print("등급: S (전설의 해제 전문가)")
    elif score >= 250:
        print("등급: A (숙련된 기술자)")
    elif score >= 150:
        print("등급: B (준수한 요원)")
    else:
        print("등급: C (초보 해제 견습생)")
    print("수고했어요!")

if __name__ == "__main__":
    try:
        game()
    except KeyboardInterrupt:
        print("\n게임 종료")

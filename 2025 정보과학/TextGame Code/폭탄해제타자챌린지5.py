# ============================================================
#  폭탄 해제 챌린지: 안정 입력(쓰레드) + 카운트다운 진행바
#  - Windows ANSI 강제 활성화 (ENABLE_VIRTUAL_TERMINAL_PROCESSING)
#  - 진행 바는 입력 줄 "위" 한 줄만 갱신 (커서 save/restore)
#  - 입력은 input()을 별도 쓰레드에서 수집
# ============================================================

import sys, time, os, random, threading, queue

# ---------- Windows에서 ANSI 활성화 ----------
def _enable_windows_ansi():
    if os.name != "nt":
        return True
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
        mode = ctypes.c_uint()
        if kernel32.GetConsoleMode(handle, ctypes.byref(mode)) == 0:
            return False
        ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
        new_mode = mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING
        if kernel32.SetConsoleMode(handle, new_mode) == 0:
            return False
        return True
    except Exception:
        return False

def _supports_ansi() -> bool:
    if not sys.stdout.isatty():
        return False
    if os.name == "nt":
        return _enable_windows_ansi()
    return True

# ---------- 쓰레드/큐 기반 안전 입력 + 진행바 ----------
def timed_input_safe(prompt="> ", limit_sec=5.0, tick=0.05, label="카운트다운"):
    """
    제한 시간 안에 입력을 받는다.
    반환: (text(str) or None, elapsed(float))
      - 시간 내 엔터 입력: (text, 경과초)
      - 시간 초과: (None, limit_sec)
    """
    use_ansi = _supports_ansi()
    start = time.time()
    deadline = start + limit_sec
    q = queue.Queue()

    # 타이머 줄과 입력 줄을 먼저 만든다
    bar_width = 28
    empty_bar = "[" + ("-" * bar_width) + "]"
    print(f"{label}: {empty_bar}   0%")
    print(prompt, end="", flush=True)

    # 입력 쓰레드
    def reader():
        try:
            text = input("")
        except EOFError:
            text = ""
        q.put((text, time.time()))

    t = threading.Thread(target=reader, daemon=True)
    t.start()

    # 타이머 그리기 (입력 줄 위 한 줄만 갱신)
    def draw(ratio):
        if not use_ansi:
            return  # ANSI가 없으면 애니메이션 생략(정확도는 유지)
        ratio = max(0.0, min(1.0, ratio))
        filled = int(bar_width * ratio)
        bar = "[" + ("█" * filled) + ("-" * (bar_width - filled)) + "]"
        pct = int(ratio * 100)

        # 커서 저장 -> 한 줄 위로 -> CR -> 타이머 줄 덮어쓰기 -> 커서 복원
        sys.stdout.write("\x1b[s")
        sys.stdout.write("\x1b[1A\r")
        sys.stdout.write(f"{label}: {bar} {pct:3d}%")
        # 남은 자국 지우기
        sys.stdout.write("\x1b[0K")
        sys.stdout.write("\x1b[u")
        sys.stdout.flush()

    # 카운트다운 루프
    while True:
        # 입력 먼저 확인
        try:
            text, tstamp = q.get_nowait()
            elapsed = tstamp - start
            if tstamp <= deadline:
                # 성공 입력
                if use_ansi:
                    draw(1.0)
                    # 타이머 줄 아래(입력 줄)로 내려와 줄바꿈
                    sys.stdout.write("\n")
                    sys.stdout.flush()
                else:
                    print()
                return text, elapsed
            else:
                # 타임업 이후 입력
                if use_ansi:
                    draw(1.0)
                    sys.stdout.write("\n")
                    sys.stdout.flush()
                else:
                    print()
                return None, limit_sec
        except queue.Empty:
            pass

        now = time.time()
        if now >= deadline:
            # 타임업
            if use_ansi:
                draw(1.0)
                sys.stdout.write("\n")
                sys.stdout.flush()
            else:
                print()
            return None, limit_sec

        if use_ansi:
            draw((now - start) / limit_sec)
        time.sleep(tick)

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

RANDOM_EVENTS = [
    ("+0.8초 보너스", +0.8),
    ("-0.7초 페널티", -0.7),
    ("점수 +30 보너스", "score:+30"),
    ("이번 라운드는 대소문자 구분", "case:on"),
]

def calc_points(limit, elapsed, correct, base=100):
    if not correct:
        return 0
    remain = max(0.0, limit - elapsed)
    ratio = remain / limit
    return base + int(80 * ratio)

def play_round(target, limit, case_sensitive=False):
    print(f"\n단어(제한 {limit:.1f}초): {target}")
    if not case_sensitive:
        print("(대소문자 구분 없음)")
    text, elapsed = timed_input_safe("> ", limit, label="카운트다운")
    if text is None:
        print("시간 초과")
        return False, elapsed, 0
    ok = (text == target) if case_sensitive else (text.strip().lower() == target.lower())
    if ok:
        print(f"정답 ({elapsed:.2f}초)")
        return True, elapsed, calc_points(limit, elapsed, True)
    else:
        print(f"오답. 정답: {target}")
        return False, elapsed, 0

def game():
    print("=== 폭탄 해제 챌린지: 안정 입력 버전 ===")
    print("레벨을 선택하세요:")
    print("  1) Easy   (7초)")
    print("  2) Normal (5초)")
    print("  3) Hard   (3.5초)")
    lv = input("번호: ").strip()
    if lv not in LEVELS:
        lv = "2"
        print("기본값 Normal로 진행합니다.")

    level_name, base_limit, words = LEVELS[lv]
    lives, score, best_time, combo, round_no = 3, 0, None, 0, 0
    print(f"\n[{level_name}] 모드 시작. 라이프 {lives}개")

    while lives > 0:
        round_no += 1
        print(f"\n----- Round {round_no} -----")
        target = random.choice(words)

        # 20% 확률 이벤트
        limit = base_limit
        case_sensitive = False
        if random.random() < 0.20:
            msg, eff = random.choice(RANDOM_EVENTS)
            print(msg)
            if isinstance(eff, (int, float)):
                limit = max(1.5, base_limit + eff)
            elif eff == "case:on":
                case_sensitive = True
            elif isinstance(eff, str) and eff.startswith("score:"):
                add = int(eff.split(":")[1])
                score += add
                print(f"(즉시 점수 +{add})")

        ok, elapsed, pts = play_round(target, limit, case_sensitive)
        if ok:
            score += pts
            combo += 1
            best_time = elapsed if (best_time is None or elapsed < best_time) else best_time
            print(f"점수 +{pts} | 누적 {score} | 콤보 {combo}")
            if combo > 0 and combo % 3 == 0:
                score += 25
                print(f"콤보 {combo}. 보너스 +25 (누적 {score})")
        else:
            lives -= 1
            combo = 0
            print(f"남은 라이프: {lives}")

        if lives > 0:
            cmd = input("계속하려면 Enter, 종료는 q: ").strip().lower()
            if cmd == "q":
                break

    print("\n===== 결과 =====")
    print(f"- 모드: {level_name}")
    print(f"- 총점: {score}")
    print(f"- 최고 반응: {best_time:.2f}초" if best_time is not None else "- 최고 반응: 기록 없음")
    if score >= 350:
        print("등급: S")
    elif score >= 250:
        print("등급: A")
    elif score >= 150:
        print("등급: B")
    else:
        print("등급: C")

if __name__ == "__main__":
    try:
        game()
    except KeyboardInterrupt:
        print("\n게임 종료")

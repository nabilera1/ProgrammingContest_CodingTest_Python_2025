# ============================================================
#  폭탄 해제 챌린지: 충돌 없는 카운트다운 + 논블로킹 입력 (단일 파일)
#  - 표준 라이브러리만 사용 (Windows: msvcrt / POSIX: termios+select)
#  - 진행 바는 입력 줄 "위" 한 줄만 갱신 (ANSI 커서 save/restore)
#  - 백스페이스/엔터/ESC(전체 지우기) 지원, 타이핑 연속 입력 OK
# ============================================================

import sys, time, os, random

# ---------- ANSI 지원 체크 ----------
def _supports_ansi():
    # 대부분의 콘솔은 True, IDLE/노트북 등은 False일 수 있음(그땐 진행 바 생략)
    return sys.stdout.isatty()

# ---------- 타이머가 입력 줄과 충돌하지 않도록 그리는 안전 입력 ----------
def timed_input_safe(prompt="> ", limit_sec=5.0, tick=0.05, label="카운트다운"):
    """
    제한 시간 내 사용자 입력을 받는다(엔터로 확정).
    반환: (text(str) or None, elapsed(float))
      - 시간 내 엔터 입력: (text, 경과초)
      - 시간 초과: (None, limit_sec)
    """
    use_ansi = _supports_ansi()
    start = time.time()
    deadline = start + limit_sec
    buf = []

    # 초기 2줄 마련: [타이머 줄] + [입력 줄]
    print(f"{label}: [------------------------]   0%")
    print(prompt, end="", flush=True)

    def draw_timer(ratio):
        if not use_ansi:
            return  # ANSI 미지원 환경(IDLE 등)에서는 진행 바 생략(입력은 정상 동작)
        # 커서 저장 -> 한 줄 위로 -> 라인 처음 -> 타임바 새로 그림 -> 커서 복원
        sys.stdout.write("\x1b[s")        # save cursor
        sys.stdout.write("\x1b[1A\r")     # up 1 line + CR
        width = 24
        ratio = max(0.0, min(1.0, ratio))
        filled = int(width * ratio)
        bar = "█" * filled + "-" * (width - filled)
        pct = int(ratio * 100)
        sys.stdout.write(f"{label}: [{bar}] {pct:3d}%")
        sys.stdout.write(" " * 5)         # 잔여 지우기용 여백
        sys.stdout.write("\x1b[u")        # restore cursor
        sys.stdout.flush()

    def redraw_input():
        # 현재 입력 줄을 안전하게 다시 그림(이 줄은 덮어쓰지 않음)
        if not sys.stdout.isatty():
            return
        sys.stdout.write("\r")  # 줄 처음
        sys.stdout.write(prompt + "".join(buf))
        sys.stdout.write("\x1b[0K")  # 나머지 지우기
        sys.stdout.flush()

    if os.name == "nt":
        # -------------------- Windows (msvcrt) --------------------
        import msvcrt
        try:
            while time.time() < deadline:
                # 타이머 갱신
                draw_timer((time.time() - start) / limit_sec)

                # 누른 키들 모두 처리
                while msvcrt.kbhit():
                    ch = msvcrt.getwch()  # 유니코드 1글자
                    if ch in ("\r", "\n"):
                        elapsed = time.time() - start
                        print()  # 입력 줄 개행
                        return "".join(buf), elapsed
                    elif ch == "\x08":  # Backspace
                        if buf:
                            buf.pop()
                            redraw_input()
                    elif ch == "\x1b":  # ESC -> 전체 지우기
                        buf.clear()
                        redraw_input()
                    else:
                        buf.append(ch)
                        redraw_input()

                time.sleep(tick)

            # 시간 초과
            draw_timer(1.0)
            print()
            return None, limit_sec

        except KeyboardInterrupt:
            print("\n^C")
            return None, time.time() - start

    else:
        # -------------------- POSIX (macOS/Linux) --------------------
        import termios, tty, select
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setcbreak(fd)  # 문자 단위 즉시 입력
            while time.time() < deadline:
                draw_timer((time.time() - start) / limit_sec)

                rlist, _, _ = select.select([sys.stdin], [], [], tick)
                if rlist:
                    ch = sys.stdin.read(1)
                    if ch in ("\r", "\n"):
                        elapsed = time.time() - start
                        print()
                        return "".join(buf), elapsed
                    elif ch in ("\x7f", "\b"):  # Backspace
                        if buf:
                            buf.pop()
                            redraw_input()
                    elif ch == "\x1b":         # ESC -> 전체 지우기
                        buf.clear()
                        redraw_input()
                    else:
                        buf.append(ch)
                        redraw_input()

            draw_timer(1.0)
            print()
            return None, limit_sec

        except KeyboardInterrupt:
            print("\n^C")
            return None, time.time() - start
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

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
    ("+0.8초 보너스! 여유가 생겼다.", +0.8),
    ("-0.7초 페널티! 긴장하세요.", -0.7),
    ("점수 +30 보너스!", "score:+30"),
    ("이번 라운드는 대문자/소문자 구분!", "case:on"),
]

# ---------- 점수 계산 ----------
def calc_points(limit, elapsed, correct, base=100):
    if not correct:
        return 0
    remain = max(0.0, limit - elapsed)
    ratio = remain / limit
    return base + int(80 * ratio)

# ---------- 한 라운드 ----------
def play_round(target, limit, case_sensitive=False):
    print(f"\n단어(제한 {limit:.1f}초): {target}")
    if not case_sensitive:
        print("(대소문자 구분 없음)")
    user, elapsed = timed_input_safe("> ", limit, label="카운트다운")

    if user is None:
        print("시간 초과!")
        return False, elapsed, 0

    ok = (user == target) if case_sensitive else (user.strip().lower() == target.lower())
    if ok:
        print(f"정답! ({elapsed:.2f}초)")
        return True, elapsed, calc_points(limit, elapsed, True)
    else:
        print(f"오답! 정답은 '{target}'")
        return False, elapsed, 0

# ---------- 전체 게임 ----------
def game():
    print("=== 폭탄 해제 챌린지: 업그레이드 (안전 입력 버전) ===")
    print("레벨을 선택하세요:")
    print("  1) Easy   (7초, 쉬운 단어)")
    print("  2) Normal (5초, 중간 단어)")
    print("  3) Hard   (3.5초, 어려운 단어)")
    level_key = input("번호: ").strip()
    if level_key not in LEVELS:
        level_key = "2"
        print("기본값 Normal로 진행합니다.")

    level_name, base_limit, words = LEVELS[level_key]
    lives, score, best_time, combo, round_no = 3, 0, None, 0, 0
    print(f"\n[{level_name}] 모드 시작! 라이프 {lives}개")

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
            print(f"점수 +{pts} | 누적 {score}점 | 콤보 {combo}")
            if combo > 0 and combo % 3 == 0:
                score += 25
                print(f"콤보 {combo}! 보너스 +25 (누적 {score})")
        else:
            lives -= 1
            combo = 0
            print(f"남은 라이프: {lives}")

        if lives > 0:
            cmd = input("계속하려면 Enter, 그만하려면 q: ").strip().lower()
            if cmd == "q":
                break

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

# ============================================================
#  폭탄 해제 챌린지: 입력 스레드 + 이중 진행바 모드(ANSI / STDERR)
#  - ANSI 가능: 입력 줄 위 한 줄만 부드럽게 갱신
#  - ANSI 불가: stderr에 같은 줄 카운트다운 표시(\r, 깜빡임 최소화)
#  - 시간 내 입력 정확 판정
# ============================================================

import sys, time, os, random, threading, queue

# ---------- Windows ANSI 활성화 ----------
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
        return kernel32.SetConsoleMode(handle, new_mode) != 0
    except Exception:
        return False

def _ansi_mode():
    # ANSI가 되면 True. 되지 않으면 False.
    if os.name == "nt":
        return _enable_windows_ansi()
    # 일부 IDE는 isatty가 False여도 ANSI를 그려줍니다. 보수적으로 True 반환.
    return True

# ---------- 진행바 렌더러: ANSI / STDERR ----------
class CountdownRenderer:
    def __init__(self, label, total_sec, width=28):
        self.label = label
        self.total = max(0.001, float(total_sec))
        self.width = width
        self._stop = threading.Event()
        self._thread = None
        self._use_ansi = _ansi_mode()

    def start_above_input(self):
        """입력 줄 위 한 줄(ANSI) 또는 stderr 한 줄 모드 시작"""
        if self._use_ansi:
            # 타이머 줄 + 입력 줄을 먼저 확보
            print(f"{self.label}: [{'-'*self.width}]   0%")
        else:
            # ANSI가 없으면 stderr에 같은 줄 진행바를 쓸 것이므로,
            # 입력 프롬프트 앞에 한 줄 구분을 출력해 가독성 확보
            sys.stderr.write(f"{self.label}: starting...\n")
            sys.stderr.flush()

        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def _draw_ansi(self, ratio):
        # 커서 저장 -> 한 줄 위로 -> CR -> 타임라인 갱신 -> 라인 지우기 -> 복원
        ratio = max(0.0, min(1.0, ratio))
        filled = int(self.width * ratio)
        bar = "[" + ("█" * filled) + ("-" * (self.width - filled)) + "]"
        pct = int(ratio * 100)
        sys.stdout.write("\x1b[s")     # save
        sys.stdout.write("\x1b[1A\r")  # up 1 line + CR
        sys.stdout.write(f"{self.label}: {bar} {pct:3d}%")
        sys.stdout.write("\x1b[0K")    # clear to EOL
        sys.stdout.write("\x1b[u")     # restore
        sys.stdout.flush()

    def _draw_stderr_inline(self, ratio):
        ratio = max(0.0, min(1.0, ratio))
        filled = int(self.width * ratio)
        bar = "[" + ("#" * filled) + ("-" * (self.width - filled)) + "]"
        pct = int(ratio * 100)
        # 같은 줄 갱신: stderr 사용. 입력 프롬프트(stdout)와 충돌을 줄임.
        sys.stderr.write("\r" + f"{self.label}: {bar} {pct:3d}%")
        sys.stderr.flush()

    def _run(self):
        start = time.time()
        while not self._stop.is_set():
            now = time.time()
            ratio = (now - start) / self.total
            if ratio >= 1.0:
                ratio = 1.0
                if self._use_ansi:
                    self._draw_ansi(ratio)
                else:
                    self._draw_stderr_inline(ratio)
                    sys.stderr.write("\n")
                    sys.stderr.flush()
                break
            if self._use_ansi:
                self._draw_ansi(ratio)
            else:
                self._draw_stderr_inline(ratio)
            time.sleep(0.05)

    def stop(self, finalize=True):
        self._stop.set()
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=0.2)
        if finalize and not self._use_ansi:
            # 줄 정리
            sys.stderr.write("\n")
            sys.stderr.flush()

# ---------- 입력: 쓰레드/큐 기반 ----------
def timed_input_safe(prompt="> ", limit_sec=5.0, label="카운트다운"):
    """
    제한 시간 내 입력을 받음.
    반환: (text(str) or None, elapsed(float))
    """
    start = time.time()
    deadline = start + limit_sec
    q = queue.Queue()

    # 진행바 시작
    renderer = CountdownRenderer(label, limit_sec)
    renderer.start_above_input()

    # 입력 프롬프트(표준 입력은 항상 stdout에 표시)
    print(prompt, end="", flush=True)

    def reader():
        try:
            txt = input("")
        except EOFError:
            txt = ""
        q.put((txt, time.time()))

    t = threading.Thread(target=reader, daemon=True)
    t.start()

    while True:
        # 입력 체크
        try:
            text, tstamp = q.get_nowait()
            elapsed = tstamp - start
            renderer.stop(finalize=True)
            # 시간 내 입력 판정
            if tstamp <= deadline:
                # ANSI 모드였으면 위 줄은 renderer가 정리. 줄 맞춤을 위해 개행.
                if renderer._use_ansi:
                    sys.stdout.write("\n")
                    sys.stdout.flush()
                return text, elapsed
            else:
                return None, limit_sec
        except queue.Empty:
            pass

        if time.time() >= deadline:
            renderer.stop(finalize=True)
            return None, limit_sec

        time.sleep(0.02)

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
        # 여기서 사용자가 실제로 입력한 값을 함께 출력
        # 숨은 문자를 확인하려면 아래 줄에서 text 대신 repr(text) 사용
        print(f"오답. 입력: {text}")
        print(f"정답: {target}")
        return False, elapsed, 0

def game():
    print("=== 폭탄 해제 챌린지: 진행바 보강 버전 ===")
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

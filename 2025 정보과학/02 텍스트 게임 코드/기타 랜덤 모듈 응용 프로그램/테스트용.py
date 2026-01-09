import random
import time


class CleaningRotation:
    def __init__(self, students):
        self.all_students = students  # 원본 명단 (변하지 않음)
        self.candidates = list(students)  # 현재 후보 명단 (계속 줄어듦)

    def pick_cleaners(self, count):
        print(f"\n[현재 남은 후보]: {len(self.candidates)}명 {self.candidates}")

        # 1. 후보가 부족하면 리셋 (로테이션 종료)
        if len(self.candidates) < count:
            print("🔄 모든 학생이 청소를 완료했습니다! 명단을 초기화합니다.")
            self.candidates = list(self.all_students)
            print(f"(명단 복구 완료: {len(self.candidates)}명)")

        # 2. 후보 중에서 무작위 추첨
        picked = random.sample(self.candidates, count)

        # 3. 뽑힌 학생을 후보 명단에서 제거 (핵심 로직)
        for student in picked:
            self.candidates.remove(student)

        return picked


# --- 실행 시뮬레이션 ---

# 전체 학생 명단
student_list = ["철수", "영희", "민수", "지수", "호영", "민지", "다혜"]
manager = CleaningRotation(student_list)

# 매일 2명씩 5일 동안 뽑는 상황 가정
day = 1
while True:
    input(f"\n📅 {day}일차 당번을 뽑으려면 Enter를 누르세요...")

    # 당번 2명 선정
    todays_cleaners = manager.pick_cleaners(2)

    print(f"🎉 오늘의 당번: {todays_cleaners}")
    print("-" * 40)

    day += 1

    # (테스트를 위해 5일차까지만 반복)
    if day > 5:
        print("\n✅ 시뮬레이션을 종료합니다.")
        break
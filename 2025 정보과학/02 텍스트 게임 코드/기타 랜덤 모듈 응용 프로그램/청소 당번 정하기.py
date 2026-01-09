import random

# 1. 청소 역할과 학생 명단 준비
roles = ["칠판 닦기", "바닥 쓸기", "대걸레", "쓰레기통", "우유 급식"]
students = ["김철수", "이영희", "박민수", "최지수", "정우성", "강동원", "아이유"]

# 2. 학생 명단을 무작위로 섞음 (공정성 확보!)
# 주의: 원본 리스트(students)의 순서가 바뀝니다.
random.shuffle(students)

# 3. 역할과 학생을 1:1로 매칭
# 역할의 개수만큼만 학생이 필요하므로, 섞인 명단 앞쪽에서 역할 수만큼 가져옵니다.
print(f"🧹 오늘의 청소 당번 ({len(roles)}명) 🧹")
print("-" * 30)

# zip 함수: 두 리스트를 지퍼처럼 하나씩 묶어줍니다.
for role, student in zip(roles, students):
    print(f"✅ {role}: {student}")

print("-" * 30)
print("나머지 학생들은 하교하세요!")
"""
문제) 숫자 추측 미니게임

[문제] 다음 조건을 만족하는 숫자 추측 프로그램을 작성하시오.
1~20 사이 무작위 정답을 만든다.
사용자는 총 5번 추측할 수 있다.
숫자가 아니면 “숫자!”를 출력하고 기회를 소모하지 않는다.
정답이면 즉시 종료, 아니면 UP/DOWN 힌트를 준다.
기회 소진 시 정답을 출력한다.
"""

import random
lo, hi, tries = 1, 20, 5
secret = random.randint(lo, hi)
print(f"{lo}~{hi} 숫자 맞히기! {tries}번 기회")
while tries > 0:
    s = input("추측: ").strip()
    if not s.isdigit():
        print("숫자!"); continue
    g = int(s)
    if g == secret:
        print("정답!")
        break
    print("UP" if g < secret else "DOWN")
    tries -= 1
if tries == 0:
    print("실패.. 정답:", secret)


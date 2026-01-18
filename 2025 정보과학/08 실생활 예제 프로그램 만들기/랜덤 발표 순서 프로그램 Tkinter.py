'''
내장 GUI 라이브러리인 Tkinter를 사용하여 작성했습니다.

웹앱과 마찬가지로 어두운 테마(Dark Mode)를 적용했고,
번호가 슬롯머신처럼 빠르게 돌아가다가 하나씩 확정되는 애니메이션 효과를 구현했습니다.

주요 기능 및 구현 방식:

Tkinter: 파이썬 기본 내장 라이브러리라 설치가 필요 없습니다.

animate_rolling 함수: root.after() 메서드를 재귀적으로 호출하여 while문 없이도 화면이 멈추지 않고 숫자가 다다닥 바뀌는 애니메이션을 구현했습니다.

디자인:

배경색 #2b2b2b (진한 회색)

강조색 #00adb5 (청록색), #ff2e63 (분홍색 - 롤링 중일 때)

카드 형태의 레이아웃을 위해 tk.Frame에 테두리(bd)와 여백(padding)을 주었습니다.

로직: random.shuffle()을 이용해 1부터 14까지의 숫자를 중복 없이 섞은 뒤, 애니메이션과 함께 순서대로 보여줍니다.
'''

import tkinter as tk
from tkinter import font
import random


class RandomDrawApp:
    def __init__(self, root):
        self.root = root
        self.root.title("발표 순서 추첨 프로그램")
        self.root.geometry("800x600")
        self.root.configure(bg="#2b2b2b")  # 배경색: 어두운 회색

        # 상태 변수 초기화
        self.total_members = 14
        self.is_running = False
        self.labels = []
        self.final_order = []

        # 타이틀 레이블
        self.title_label = tk.Label(
            root,
            text="발표 순서 추첨",
            font=("Arial", 24, "bold"),
            bg="#2b2b2b",
            fg="#ffffff"
        )
        self.title_label.pack(pady=20)

        # 결과가 표시될 그리드 프레임
        self.grid_frame = tk.Frame(root, bg="#2b2b2b")
        self.grid_frame.pack(pady=20)

        # 1번부터 14번까지의 카드(레이블) 생성
        self.create_cards()

        # 추첨 시작 버튼
        self.start_button = tk.Button(
            root,
            text="추첨 시작",
            command=self.start_draw,
            font=("Arial", 16, "bold"),
            bg="#00adb5",  # 버튼 배경: 청록색
            fg="white",  # 버튼 글자: 흰색
            activebackground="#007a80",
            activeforeground="white",
            width=20,
            height=2,
            bd=0,
            relief="flat"
        )
        self.start_button.pack(pady=30)

    def create_cards(self):
        # 14개의 번호판을 2줄로 나누어 배치 (7개씩 2줄)
        rows = 2
        cols = 7

        for i in range(self.total_members):
            row = i // cols
            col = i % cols

            # 개별 카드 프레임
            card_frame = tk.Frame(
                self.grid_frame,
                bg="#393e46",
                bd=2,
                relief="solid",
                width=100,
                height=120
            )
            card_frame.grid(row=row, column=col, padx=10, pady=10)
            card_frame.grid_propagate(False)  # 크기 고정

            # 순위 표시 (예: 1번째)
            rank_label = tk.Label(
                card_frame,
                text=f"{i + 1}번째",
                font=("Arial", 10),
                bg="#393e46",
                fg="#aaaaaa"
            )
            rank_label.pack(pady=(15, 5))

            # 추첨된 번호 표시 (초기값 ?)
            num_label = tk.Label(
                card_frame,
                text="?",
                font=("Arial", 28, "bold"),
                bg="#393e46",
                fg="#ffffff"
            )
            num_label.pack()

            self.labels.append({
                'frame': card_frame,
                'num_text': num_label,
                'rank_text': rank_label
            })

    def start_draw(self):
        if self.is_running:
            return

        self.is_running = True
        self.start_button.config(state="disabled", text="추첨 진행 중...", bg="#555555")

        # 1~14 리스트 생성 및 랜덤 섞기
        self.final_order = list(range(1, self.total_members + 1))
        random.shuffle(self.final_order)

        # 모든 카드를 초기 상태로 리셋
        for item in self.labels:
            item['num_text'].config(text="?", fg="#ffffff")
            item['frame'].config(bg="#393e46", bd=2)
            item['rank_text'].config(bg="#393e46", fg="#aaaaaa")
            item['num_text'].config(bg="#393e46")

        # 첫 번째 순서부터 공개 시작
        self.reveal_next(0)

    def reveal_next(self, index):
        # 모든 순서 공개가 끝났을 때
        if index >= self.total_members:
            self.is_running = False
            self.start_button.config(state="normal", text="다시 추첨하기", bg="#00adb5")
            return

        # 현재 추첨할 대상
        target = self.labels[index]
        target_number = self.final_order[index]

        # 롤링 애니메이션 효과 (약 0.5초~1초 동안 랜덤 숫자 보여주기)
        # rolling_count: 숫자가 바뀌는 횟수
        self.animate_rolling(index, target, target_number, rolling_count=15)

    def animate_rolling(self, index, target_item, final_number, rolling_count):
        # 롤링이 끝났을 때 -> 최종 번호 확정
        if rolling_count <= 0:
            target_item['num_text'].config(text=str(final_number), fg="#00adb5")  # 확정 색상(청록)
            target_item['frame'].config(bd=4, bg="#222831")  # 테두리 강조

            # 다음 순서로 넘어감 (약간의 딜레이 후)
            self.root.after(300, lambda: self.reveal_next(index + 1))
            return

        # 롤링 중 -> 랜덤 숫자 표시
        random_num = random.randint(1, self.total_members)
        target_item['num_text'].config(text=str(random_num), fg="#ff2e63")  # 롤링 중 색상(분홍)

        # 재귀 호출로 애니메이션 구현 (속도 조절: 50ms 마다 갱신)
        self.root.after(50, lambda: self.animate_rolling(index, target_item, final_number, rolling_count - 1))


if __name__ == "__main__":
    root = tk.Tk()
    app = RandomDrawApp(root)
    root.mainloop()
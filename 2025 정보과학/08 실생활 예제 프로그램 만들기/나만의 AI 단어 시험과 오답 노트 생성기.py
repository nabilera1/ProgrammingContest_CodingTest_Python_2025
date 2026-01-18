'''
<나만의 AI 단어 시험 & 오답 노트 생성기> 기획서에 맞춰, 고등학생 수준에서 이해하고 활용할 수 있는 파이썬 예시 코드를 작성해 드립니다.

이 코드는 리스트, 딕셔너리(자료구조), 반복문, 그리고 파일 입출력 기능을 모두 포함하고 있어 수행평가용으로 적합합니다.

[Python Code] Voca Master (단어 시험기)
코드 분석 및 평가 포인트 (선생님용 가이드)
학생들이 코드를 제출했을 때, 다음 포인트들을 잘 구현했는지 확인하시면 됩니다.

import random과 shuffle: 문제를 매번 다르게 섞어서 내는지? (기획서의 '랜덤 출제' 기능)

딕셔너리(dict) 활용: 단어와 뜻을 쌍(Key-Value)으로 잘 관리하고 있는지?

strip() 함수: 사용자가 실수로 입력한 공백을 처리해 주는 디테일이 있는지? (사용자 편의성)

파일 입출력(open, write): 프로그램이 종료된 후에도 결과(오답)가 컴퓨터에 남도록 구현했는지? (고등 수준 핵심)

심화 과제 제안 (변별력 주기)
상위권 학생들에게는 다음과 같은 기능을 추가해 보라고 제안해 보세요.

LV 1: 단어 데이터를 코드 안에 적지 말고, voca.txt 파일에서 읽어오게 만들기.

LV 2: time 모듈을 이용해 '3초 안에 입력 못하면 오답 처리' 하는 타임 어택 기능 추가.

LV 3: 파이썬 tkinter를 사용하여 검은 화면(콘솔)이 아닌 윈도우 창이 뜨는 GUI 프로그램으로 만들기.


'''

import random
import time


def main():
    # 1. 학습할 단어장 데이터 (실제 수행평가에서는 파일에서 읽어오기로 구현 가능)
    # 형식: {'영어단어': '한글뜻'}
    voca_book = {
        'artificial': '인공의',
        'intelligence': '지능',
        'variable': '변수',
        'function': '함수',
        'loop': '반복',
        'condition': '조건',
        'algorithm': '알고리즘',
        'analysis': '분석'
    }

    # 틀린 단어를 저장할 리스트
    wrong_answers = []

    print("=" * 40)
    print(f"Voca Master 단어 시험을 시작합니다.")
    print(f"총 {len(voca_book)}개의 문제가 출제됩니다.")
    print("=" * 40)
    time.sleep(1)  # 1초 대기 (긴장감 조성)

    # 2. 문제 출제 알고리즘 (딕셔너리를 리스트로 변환하여 섞기)
    quiz_list = list(voca_book.keys())
    random.shuffle(quiz_list)  # 순서를 무작위로 섞음

    score = 0

    # 3. 반복문으로 퀴즈 진행
    for i, word in enumerate(quiz_list):
        print(f"\n[문제 {i + 1}] '{word}'의 뜻은 무엇일까요?")
        user_answer = input("답 입력 > ").strip()  # 공백 제거

        correct_answer = voca_book[word]

        # 정답 비교
        if user_answer == correct_answer:
            print("정답입니다!")
            score += 1
        else:
            print(f"틀렸습니다. (정답: {correct_answer})")
            # 틀린 단어와 정답을 튜플 형태로 저장
            wrong_answers.append((word, correct_answer))

    # 4. 결과 출력
    print("\n" + "=" * 40)
    print(f"시험 종료! 당신의 점수는 {score}/{len(voca_book)} 점입니다.")

    # 5. 오답 노트 파일 생성 (파일 입출력)
    if wrong_answers:
        print("오답이 있어 'wrong_note.txt' 파일을 생성합니다...")

        # 'w' 모드는 파일을 쓸 때 사용 (utf-8 인코딩 필수)
        with open("wrong_note.txt", "w", encoding="utf-8") as file:
            file.write(f"[ 오답 노트 - {time.strftime('%Y-%m-%d')} ]\n\n")
            for word, meaning in wrong_answers:
                file.write(f"단어: {word:<15} | 뜻: {meaning}\n")

        print("오답 노트 저장 완료! 파일을 확인해보세요.")
    else:
        print("축하합니다! 만점이라 오답 노트가 없습니다.")


if __name__ == "__main__":
    main()

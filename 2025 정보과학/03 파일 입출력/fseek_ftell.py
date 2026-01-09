# 예시 파일 만들기
with open("sample.txt", "w") as f:
    f.write("Hello\nPython\nWorld")

# 파일 읽기
with open("sample.txt", "r") as f:
    print("처음 위치:", f.tell())  # 처음은 0 (파일 맨 앞)

    data = f.readline()   # 한 줄 읽기
    print("첫 줄 데이터 :", data)
    print("읽은 데이터:", data.strip())
    print("현재 위치:", f.tell())  # 파일 포인터가 이동함

    f.seek(0)             # 다시 맨 앞으로 이동
    print("seek(0) 이후 위치:", f.tell())

    data = f.read(5)      # 처음부터 5글자 읽기
    print("다시 읽은 데이터:", data)
    print("최종 위치:", f.tell())

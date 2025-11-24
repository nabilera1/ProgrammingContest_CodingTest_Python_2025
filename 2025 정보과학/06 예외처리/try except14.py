# f = open("나없는파일", 'r')
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)


# try:
#     ...
# except [발생오류 [as 오류변수]]:
#     ...


try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError as e:
    print("인덱싱 할 수 없습니다.")
    print(e)

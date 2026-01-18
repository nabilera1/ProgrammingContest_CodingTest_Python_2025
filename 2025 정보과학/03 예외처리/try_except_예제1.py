# 예외 만들기
# 프로그램을 수행하다가 특수한 경우에만 예외 처리를 하려고 종종 예외를 만들어서 사용한다.
# 예외는 다음과 같이 파이썬 내장 클래스인 Exception 클래스를 상속하여 만들 수 있다.

class MyError(Exception):
    pass


def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)


say_nick("천사")
say_nick("바보")


# Traceback (most recent call last):
#   File "...", line 11, in <module>
#     say_nick("바보")
#   File "...", line 7, in say_nick
#     raise MyError()
# __main__.MyError


def add(a, b):
    return a+b

def sub(a, b):
    return a-b



print(add(1, 4))
print(sub(4, 2))


""" 다른 파일에서 
from mymath1 import add, sub
이렇게 사용했을 때는 아래와 같이 만들어야함. 참고"""
#
# if __name__ == '__main__':
#     print(add(3, 4))
#     print(sub(3, 4))



"""
__name__ 변수란?

파이썬의 __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름이다. 
만약 C:\doit>python mod1.py처럼 직접 mod1.py 파일을 실행할 경우, 
mod1.py의 __name__ 변수에는 __main__ 값이 저장된다. 
하지만 파이썬 셸이나 다른 파이썬 모듈에서 mod1을 import할 경우에는 
mod1.py의 __name__ 변수에 mod1.py의 모듈 이름인 mod1이 저장된다.

>>> import mod1
>>> mod1.__name__
'mod1'


"""
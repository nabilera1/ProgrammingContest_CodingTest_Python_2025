# class Cookie:
#     def __init__(self):
#         print(id(self))
#
# a = Cookie()
# b = Cookie()
#
# def __repr__(self):
#     return f'repr 자동 호출 {id(self)}'
#
# def __str__(self):
#     return f'str 자동 호출 ** {id(self)}'
# print(f'a = {a}')
# print(f'b = {b}')
#
#
# print(type(a))
# print(type(b))

'''
제공해주신 코드는 __repr__과 __str__이 클래스 밖에 정의되어 있어서 제대로 작동하지 않습니다.

이 두 메서드를 클래스 안으로 넣고, 두 메서드의 차이가 확연히 드러나는 '초코 쿠키' 예제로 변경

'''
class Cookie:
    def __init__(self, flavor, price):
        self.flavor = flavor
        self.price = price

    # 1. __str__: 고객(일반 사용자)을 위한 안내판
    # 목적: "예쁘고 읽기 편하게 보여주자"
    def __str__(self):
        return f"🍪 {self.flavor}맛 쿠키 ({self.price}원)"

    # 2. __repr__: 개발자(동료)를 위한 설계도
    # 목적: "이 객체가 정확히 어떻게 생겼는지 보여주자 (복붙하면 객체 생성 가능하게)"
    def __repr__(self):
        return f"Cookie(flavor='{self.flavor}', price={self.price})"

# --- 실행 ---
my_cookie = Cookie("초코", 1500)

print("1. print() 함수를 쓸 때 (__str__ 호출)")
print(my_cookie)
# 출력: 🍪 초코맛 쿠키 (1500원)

print("\n2. 리스트에 담거나 repr()을 쓸 때 (__repr__ 호출)")
print([my_cookie])      # 리스트 안에 있을 때는 repr이 나옴
print(repr(my_cookie))  # 명시적으로 repr 호출
# 출력: [Cookie(flavor='초코', price=1500)]
# 출력: Cookie(flavor='초코', price=1500)


'''
구분,  __str__ (String),      __repr__ (Representation)
비유,  카페 메뉴판,             상품 바코드/성분표
대상,   손님 (일반 사용자),      공장 직원 (개발자)
목적, """맛있는 초코 쿠키입니다~"" (친절함)",     """제품명:Cookie, 속성:초코, 가격:1500"" (정확함)"
호출,  print(a),             "[a], a (콘솔 입력), repr(a)"

'''
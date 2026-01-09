non_ascii_str = "안녕하세요, 세계!"

# ascii() 함수를 사용한 이스케이프된 형태로 변환
escaped_str = ascii(non_ascii_str)

print(escaped_str)
# '\uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!'


non_ascii_str = "Hello, 세계!"

# ascii() 함수를 사용한 이스케이프된 형태로 변환
escaped_str = ascii(non_ascii_str)

print(escaped_str)
# 'Hello, \uc138\uacc4!'
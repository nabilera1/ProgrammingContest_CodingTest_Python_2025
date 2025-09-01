# 2진수 문자열 → 10진수
binary = "1010"   # 2진수 1010
print(int(binary, 2))   # 출력: 10

# 8진수 문자열 → 10진수
octal = "17"      # 8진수 17
print(int(octal, 8))    # 출력: 15

# 16진수 문자열 → 10진수
hexadecimal = "1F"  # 16진수 1F
print(int(hexadecimal, 16))  # 출력: 31



# 10진수를 다른 진법으로 변환
num = 31

print(bin(num))  # 2진수: 0b11111
print(oct(num))  # 8진수: 0o37
print(hex(num))  # 16진수: 0x1f


# int("문자열", base) → base 진법 문자열을 10진수로 변환
#
# bin(), oct(), hex() → 10진수를 다른 진법 문자열로 변환
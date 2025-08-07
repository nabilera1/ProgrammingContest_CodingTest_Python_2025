# import sys
# input = sys.stdin.readline

T = int(input())
zero = [0] * 41
one = [0] * 41

zero[0] = 1
one[1] = 1

for i in range(2, 41):
    zero[i] = zero[i - 1] + zero[i - 2]
    one[i] = one[i - 1] + one[i - 2]

inputs = [int(input()) for _ in range(T)]
for num in inputs:
    print(zero[num], one[num])


# import sys
# input = sys.stdin.readline
#
# T = int(input())
# zero = [0] * 41
# one = [0] * 41
#
# zero[0] = 1
# one[1] = 1
#
# for i in range(2, 41):
#     zero[i] = zero[i - 1] + zero[i - 2]
#     one[i] = one[i - 1] + one[i - 2]
#
# inputs = [int(input().strip()) for _ in range(T)]
# # .strip() \n 포함된 것 제거하기 위해
# # 이 코드에서 sys.stdin.readline() 쓴 경우라 반드시 필요
# # 안쓰면 런타임에러 발생
# for num in inputs:
#     print(zero[num], one[num])
# 원래 숫자 리스트
numbers = [1, 2, 3, 4, 5]

# 접두사 합을 저장할 리스트
prefix_sum = [0] * len(numbers)

# 첫 번째 값은 그대로 복사
prefix_sum[0] = numbers[0]

# 나머지는 앞의 접두사 합 + 현재 숫자
for i in range(1, len(numbers)):
    prefix_sum[i] = prefix_sum[i - 1] + numbers[i]

print("접두사 합:", prefix_sum)


# prefix_sum = [0] * len(numbers)
#
# prefix_sum[0] = numbers[0]
# for i in range(1, len(numbers)):
#     prefix_sum[i] = prefix_sum[i-1]+numbers[i]
#
# print
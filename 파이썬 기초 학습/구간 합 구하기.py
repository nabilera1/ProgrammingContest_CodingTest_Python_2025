# 구간 합 공식:
# sum(i~j) = prefix_sum[j] - prefix_sum[i-1]

# 구간 합 함수
def range_sum(prefix_sum, start, end):
    if start == 0:
        return prefix_sum[end]
    else:
        return prefix_sum[end] - prefix_sum[start - 1]


numbers = [1, 2, 3, 4, 5]

# 접두사 합을 저장할 리스트
prefix_sum = [0] * len(numbers)

# 첫 번째 값은 그대로 복사
prefix_sum[0] = numbers[0]

# 나머지는 앞의 접두사 합 + 현재 숫자
for i in range(1, len(numbers)):
    prefix_sum[i] = prefix_sum[i - 1] + numbers[i]

# print("접두사 합:", prefix_sum)

print("2번째~4번째 구간 합:", range_sum(prefix_sum, 1, 3))  # 2+3+4



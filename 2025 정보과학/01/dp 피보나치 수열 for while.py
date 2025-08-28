
n = int(input("n 입력: "))

# DP 테이블 초기화 (n+1 크기, 인덱스 맞추기 위함)
dp = [0] * (n + 1)

# 기본값 설정
# dp[0] = 0
# if n >= 1:
#     dp[1] = 1

dp = [0, 1]
def fibo_dp(n):
    # 점화식 이용해서 채워넣기
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2] # IndexError: list assignment index out of range

    return dp[n]  # n번째 피보나치 수 반환

print(fibo_dp(n))

n = int(input("n 입력: "))

# dp[0] = 0, dp[1] = 1로 초기화
dp = [0, 1] + [-1] * (n - 1)  # 길이를 n+1로 맞춰줌


def fibo_dp(n):
    # 이미 계산된 값이면 그대로 반환
    if dp[n] != -1:
        return dp[n]

    # 새로 계산하고 저장
    dp[n] = fibo_dp(n - 1) + fibo_dp(n - 2)
    return dp[n]


print(fibo_dp(n))

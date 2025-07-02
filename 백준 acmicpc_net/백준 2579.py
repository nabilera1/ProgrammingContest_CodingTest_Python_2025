# https://www.acmicpc.net/problem/2579
# 계단 오르기의 규칙:
# 한 번에 1칸 또는 2칸만 올라갈 수 있다.
# 연속된 3계단은 밟을 수 없다.
# 마지막 계단은 반드시 밟아야 한다.

# 테스트용
# n = 6
# score = [0, 10, 20, 15, 25, 10, 20]

# 답안 제출시 아래 활용하세요
# n = int(input())
# score = [0] + [int(input()) for _ in range(n)]


# 테스트용
n = 4
score = [0, 9, 8, 2, 1] # 18이 최대인 경우

dp = [0] * (n+1)
# 계단 개수에 따라 분기 처리
if n == 1:
    dp[1] = score[1]
elif n == 2:
    dp[2] = score[1] + score[2]
else:
    dp[1] = score[1]
    dp[2] = score[1] + score[2]
    for i in range(3, n + 1):
        # 두 가지 방법 중 큰 점수 선택
        dp[i] = max(dp[i - 2], dp[i - 3] + score[i - 1]) + score[i]

print(dp[n])


#예제 입력 1
# 3 10
# 1
# 2
# 5
#
# 예제 출력 1
# 10

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [0] * (k+1)
dp[0] = 1 # 0원을 만드는 방법은 1개

for coin in coins:
    for j in range(coin, k+1):
        dp[j] += dp[j - coin]
        # dp[i - coin]을 가져오는 이유?
        # i - coin원을 만든 뒤, coin원을 하나 더 추가하면 i원을 만들 수 있음!

print(dp[k])


n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [0] * (k+1)
dp[0] = 1

for coin in coins:
    for j in range(coin, k+1):
        dp[j] = dp[j] + dp[j-coin]
        '''
        dp1 = 1
        dp2 = dp1에 dp0 그래서 2
        
        '''

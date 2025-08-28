dp=[0] * (n+1)

def fibo(n):
    if n <= 1: return n

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(fibo(100))
print(fibo(50))

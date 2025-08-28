n = int(input())

dp = [0,1]

def fibo(n):
    if n <= 1: return n

    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]

print(fibo(n))

print(fibo(10)) # n을 10 이상으로 처음 실행하기, IndexError: list assignment index out of range
print(fibo(5))

# dp = [0, 1]  # 기본값 준비
#
# def fibo(n):
#     while len(dp) <= n:
#         dp.append(dp[-1] + dp[-2])
#     return dp[n]
#
# print(fibo(10))  # 55
# print(fibo(5))   # 5
# print(fibo(20))  # 6765
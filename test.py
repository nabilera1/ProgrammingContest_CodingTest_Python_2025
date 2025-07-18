n, k = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]

dp = [0] * (k + 1)
print(items)
print(dp)

items = [tuple(map(int, input().split())) for _ in range(n)]

for w, v in items:
    for j in range(k, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[k])
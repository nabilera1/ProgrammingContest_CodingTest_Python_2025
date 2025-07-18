n, k = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]

# dp[j]: 현재 무게 j일 때의 최대 가치
dp = [0] * (k + 1)
# n, k 4, 7
# weight, value list [(6, 13), (4, 8), (3, 6), (5, 12)]
# dp [0, 0, 0, 0, 0, 0, 0, 0]

for weight, value in items:
    for j in range(k, weight - 1, -1):  # 무게 j부터 감소시키며 갱신
        dp[j] = max(dp[j], dp[j - weight] + value)

print(dp[k])
# 10
# 2 1 -4 3 4 -4 6 5 -5 1

# 출력 14

n = int(input())
arr = list(map(int, input().split()))

dp = arr[:]
for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1] + arr[i])

print(max(dp))

# n = int(input())
# arr = list(map(int, input().split()))
# dp = arr[:]  # 초깃값은 자기 자신
#
# # 추가: 어디서 이어왔는지 추적(-1이면 새로 시작)
# prev = [-1] * n
#
# for i in range(1, n):
#     if dp[i - 1] + arr[i] >= arr[i]:
#         dp[i] = dp[i - 1] + arr[i]
#         prev[i] = i - 1       # i-1에서 이어옴
#     else:
#         dp[i] = arr[i]
#         prev[i] = -1          # i에서 새로 시작
#
# # 최대 합의 끝 인덱스 찾기
# end = max(range(n), key=lambda i: dp[i])
# best = dp[end]
#
# # 시작 인덱스 복원
# start = end
# while prev[start] != -1:
#     start = prev[start]
#
# print(best)
# print(start, end)           # 구간 인덱스(0-based)
# print(*arr[start:end+1])    # 실제 부분배열(원하면)

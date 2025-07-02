# dp[i]를 채우면서 어디서 왔는지(backtracking 정보)도 함께 기록
# 추적용 배열 path[i] 또는 prev[i]를 사용하여 이전 계단 번호 저장
# 마지막 계단에서 시작하여 prev[i]를 따라 거꾸로 이동
# [입력]
# 6
# 10
# 20
# 15
# 25
# 10
# 20
# [출력]
# 75
# n = int(input())
# score = [0] + [int(input()) for _ in range(n)]
#
# dp = [0] * (n + 1)
# prev = [0] * (n + 1)
#
# if n >= 1:
#     dp[1] = score[1]
#     prev[1] = 0
# if n >= 2:
#     dp[2] = score[1] + score[2]
#     prev[2] = 1
#
# for i in range(3, n + 1):
#     if dp[i - 2] > dp[i - 3] + score[i - 1]:
#         dp[i] = dp[i - 2] + score[i]
#         prev[i] = i - 2
#     else:
#         dp[i] = dp[i - 3] + score[i - 1] + score[i]
#         prev[i] = i - 1  # 이전 계단 i-1 저장
#
# print(dp[n])
#
# path = []
# cur = n
# while cur > 0:
#     path.append(cur)
#     cur = prev[cur]
#
# path.reverse()
# print('경로:', path)

n = int(input())
score = [0] + [int(input()) for _ in range(n)]

dp = [0] * (n + 1)
prev = [0] * (n + 1)

if n >= 1:
    dp[1] = score[1]
    prev[1] = 0
if n >= 2:
    dp[2] = score[1] + score[2]
    prev[2] = 1

for i in range(3, n + 1):
    if dp[i - 2] > dp[i - 3] + score[i - 1]:
        dp[i] = dp[i - 2] + score[i]
        prev[i] = i - 2
    else:
        dp[i] = dp[i - 3] + score[i - 1] + score[i]
        prev[i] = i - 1  # 그냥 i-1만 저장 (추적은 prev만 따름)

# 정답 출력
print(dp[n])

# 경로 추적
path = []
cur = n
while cur > 0:
    path.append(cur)
    cur = prev[cur]

path.reverse()
print('경로:', path)


# 6
# 10
# 20
# 15
# 25
# 10
# 20
# [출력]
# 75
# 경로: [1, 2, 4, 6]
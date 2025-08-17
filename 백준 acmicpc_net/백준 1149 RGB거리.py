'''
3
26 40 83
49 60 57
13 89 99

96
'''

import sys

def main():
    input = sys.stdin.readline

    N = int(input().strip())              # 집의 개수
    cost = [list(map(int, input().split())) for _ in range(N)]  # 각 집을 R,G,B로 칠할 때 비용

    # dp[i][c] = i번째 집까지 칠했을 때,
    #            i번째 집을 색 c(0=R,1=G,2=B)로 칠하는 조건에서의 최소 총비용
    dp = [[0]*3 for _ in range(N)]

    # 1번째 집(인덱스 0)은 그냥 그 색의 비용이 곧 최솟값
    dp[0][0] = cost[0][0]  # R
    dp[0][1] = cost[0][1]  # G
    dp[0][2] = cost[0][2]  # B

    # 2번째 집부터 N번째 집까지 순서대로 채우기
    for i in range(1, N):
        # 현재 집을 R로 칠하려면 이전 집은 G 또는 B여야 함
        dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])

        # 현재 집을 G로 칠하려면 이전 집은 R 또는 B
        dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])

        # 현재 집을 B로 칠하려면 이전 집은 R 또는 G
        dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])

    # 마지막 집에서 세 색 중 최솟값이 전체 최소 비용
    print(min(dp[N-1]))

if __name__ == "__main__":
    main()

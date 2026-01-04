# import sys
#
# # 재귀 깊이 제한을 늘려줍니다. (파이썬 기본값은 1000이라 N=1000일 때 위험할 수 있음)
# sys.setrecursionlimit(2000)
#
# def dfs(graph, v, visited):
#     # 1. 현재 방을 방문 처리하고 출력합니다.
#     visited[v] = True
#     print(v, end=' ')
#
#     # 2. 현재 방과 연결된 방들을 작은 번호부터 순서대로 확인합니다.
#     for i in graph[v]:
#         # 3. 아직 방문하지 않은 방이 있다면
#         if not visited[i]:
#             # 4. 즉시 그 방으로 이동하여 로직을 재귀적으로 수행합니다. (깊게 들어감)
#             dfs(graph, i, visited)
#
# # 입력 처리
# input = sys.stdin.readline
# N, M, V = map(int, input().split())
#
# graph = [[] for _ in range(N + 1)]
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# # 번호가 작은 것부터 방문하기 위해 정렬
# for i in range(1, N + 1):
#     graph[i].sort()
#
# visited = [False] * (N + 1)
#
# # 탐색 시작
# dfs(graph, V, visited)

# input 2 4 5 7 8 10 11 12 13 14 15 1
n = int(input())
arr = list(map(int, input().split()))
dp = arr[:]  # 초깃값은 자기 자신

for i in range(1, n):
    dp[i] = max(arr[i], dp[i - 1] + arr[i])

print(max(dp))

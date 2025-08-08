'''
5 21
5 6 7 8 9

출력
첫째 줄에 M을 넘지 않으면서
M에 최대한 가까운 카드 3장의 합을 출력.
21
'''

# N, M = map(int, input().split())
# cards = list(map(int, input().split()))
# best_sum = 0
#
# for i in range(N):
#     for j in range(i+1, N):
#         for k in range(j+1, N):
#             total = cards[i] + cards[j] + cards[k]
#             if total <= M:
#                 best_sum = max(best_sum, total)
# print(best_sum)

from itertools import combinations
N, M = map(int, input().split())
cards = list(map(int, input().split()))

best = 0
for comb in combinations(cards, 3):
    total = sum(comb)
    if total <= M:
        best = max(best, total)
print(best)
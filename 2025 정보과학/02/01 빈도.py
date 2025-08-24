'''
상위 K 단어 빈도

아이디어

딕셔너리(또는 Counter)로 빈도 집계 → (-빈도, 단어) 기준으로 정렬 후 앞에서 k개.

음수 빈도를 쓰면 파이썬의 오름차순 정렬로 “빈도 내림차순”을 흉내낼 수 있음.
'''
import sys
from collections import Counter
input = sys.stdin.readline
n, k = map(int, input().split())
words = input().split()  # 남은 모든 단어 읽기

freq = Counter(words)  # 단어별 빈도수 집계

# 정렬 기준: (-빈도, 단어)
order = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

# 상위 k개 단어 출력
for i in range(k):
    print(order[i][0])

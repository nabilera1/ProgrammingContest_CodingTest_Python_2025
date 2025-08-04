import sys
input = sys.stdin.readline

# 공유기 사이의 최소 거리가 d일 때, C개의 공유기를 설치할 수 있는지
# 확인하여 True 또는 False를 반환하는 함수

# 5 3
# 1
# 2
# 8
# 4
# 9

# 3
def is_possible(houses, d, c):
    cnt = 1
    prev = houses[0]
    for house in houses[1:]:
        if house - prev >= d:
            cnt += 1
            prev = house
    return cnt >= c

n, c = map(int, input().split())
houses = sorted(int(input()) for _ in range(n)) # 제너레이터 표현식
low = 1 # 공유기 간 최소 거리 후보는 최소 1 이상
high = houses[-1] - houses[0]

ans = 0
while low <= high:
    mid = (low + high) // 2

    if is_possible(houses, mid, c):
        ans = mid
        low = mid + 1
    else:
        high = mid - 1

print(ans)


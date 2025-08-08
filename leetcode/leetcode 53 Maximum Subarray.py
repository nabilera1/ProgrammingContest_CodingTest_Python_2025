
class Solution:
    def maxSubArray(self, arr: list[int]) -> int:
        n = len(arr)
        dp = arr[:]
        for i in range(1, n):
            dp[i] = max(arr[i], dp[i-1] + arr[i])
        return max(dp)

'''
nums = [5,4,-1,7,8]
print(maxSubArray(nums))  # 출력: 23
# 최대 부분배열: [5, 4, -1, 7, 8]
'''



# class Solution:
#     def maxSubArray(self, nums: list[int]) -> int:
#         cur_sum = max_sum = nums[0]
#         for x in nums[1:]:
#             cur_sum = max(x, cur_sum + x)
#             max_sum = max(max_sum, cur_sum)
#         return max_sum

'''
설명
cur_sum → 현재 위치에서 끝나는 최대 부분합
max_sum → 지금까지 본 전체 최대 부분합
max(x, cur_sum + x) → 이전 합에 현재 값을 붙일지, 새로 시작할지 결정
최종적으로 max_sum 반환

시간·공간 복잡도
시간: O(n)
공간: O(1)


nums = [5,4,-1,7,8]
print(maxSubArray(nums))  # 출력: 23
# 최대 부분배열: [5, 4, -1, 7, 8]
'''
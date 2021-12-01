# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        # if there are no houses, return 0.
        if not nums:
            return 0
        # if there is only one house, rob it and return the value.
        if len(nums) == 1:
            return nums[0]
        # if there are two houses, rob the one with more money return the value.
        if len(nums) == 2:
            return max(nums)
        
        # if there are more than two houses, return the max of value:
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        L = len(nums)
        a, b = nums[0], max(nums[0], nums[1])
        
        for i in range(2, L):
            a, b = b, max(a + nums[i], b)
        
        return b

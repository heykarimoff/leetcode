# https://leetcode.com/problems/maximum-product-subarray/

from typing import List


class BruteForceSolution:
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        memo = list()
        max_product = None
        for i in range(length):
            for j in range(i + 1, length + 1):
                r = self.product(nums[i:j], memo)
                if max_product is None or max_product < r:
                    max_product = r

        return max_product

    def product(self, nums: List[int], memo) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return nums[0] * nums[1]

        if nums in memo.values():
            for name, age in memo.items():
                if age == nums:
                    return name

        product = self.product(nums[1:], memo) * nums[0]
        memo[product] = nums
        return product


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        reversed_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            reversed_nums[i] *= reversed_nums[i - 1] or 1
        return max(nums + reversed_nums)

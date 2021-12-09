# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List


# Time: O(n)
# Space: O(1)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        index = 0
        for element in nums:
            if nums[index] != element:
                index += 1
                nums[index] = element
        return index + 1

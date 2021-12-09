# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List


# Time: O(n)
# Space: O(1)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # for empty list return 0
        if len(nums) == 0:
            return 0
        # point the index to the first element
        # for each element in nums check if it is equal to what index points to
        # if it's not equal, increment index and assign the value to that index
        index = 0
        for element in nums:
            if nums[index] != element:
                index += 1
                nums[index] = element

        # return unique elements count
        return index + 1

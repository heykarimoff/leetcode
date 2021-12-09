# https://leetcode.com/problems/remove-element/

from typing import List

# Time: O(n)
# Space: O(1)


class SolutionWithWhileLoop:
    def removeElement(self, nums: List[int], val: int) -> int:
        # if empyt list return 0
        if len(nums) == 0:
            return 0
        # start from index 0
        # for each element in list if element is equal to val the skip it
        # else replace the value index is pointing to with element
        # and increment index
        index = 0
        for element in nums:
            if element == val:
                continue
            nums[index] = element
            index += 1

        # return the length of the list
        return index


class SolutionWithForLoop:
    def removeElement(self, nums: List[int], val: int) -> int:
        # start from index 0
        # for each element in list, if element is equal to val delete it
        # else just increment index
        index = 0
        while index < len(nums):
            if nums[index] == val:
                del nums[index]
            else:
                index += 1
        return len(nums)


class OneLineSolution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # While there is val in nums, keep removing it
        while val in nums:
            nums.remove(val)

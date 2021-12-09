# https://leetcode.com/problems/two-sum/

from typing import List

# Time: O(n^2)
# Space: O(1)


class BruteForceSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# Time: O(n)
# Space: O(n)


class HashMapSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # hash map of key: num, value: index

        # for each num in nums, check if the difference is in seen
        for i, n in enumerate(nums):
            # if second number is already seen in the hash map,
            # then return the indices
            # otherwise add the number to the hash map.
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i

        return []

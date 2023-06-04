# tag: favourite
# Given an integer array nums, return true if there exists a triple of indices
# (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
# If no such indices exists, return false.
#
# Example 1:
# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
#
# Example 2:
#
# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
#
# Example 3:
#
# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.


from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # min on left of the element including the  element
        min_on_left = [0 for _ in nums]
        min_on_left[0] = nums[0]
        for i in range(1, len(nums)):
            min_on_left[i] = min(min_on_left[i - 1], nums[i])

        # max on right for every position including self
        max_on_right = [0 for _ in nums]
        max_on_right[-1] = nums[-1]
        for i in range(len(nums) - 1 - 1, -1, -1):
            max_on_right[i] = max(max_on_right[i + 1], nums[i])

        for i, num in enumerate(nums):
            if min_on_left[i] < num and num < max_on_right[i]:
                return True

        return False

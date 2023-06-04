# Given an integer array nums, move all 0's to the end of it while maintaining the
# relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
#
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Example 2:
# Input: nums = [0]
# Output: [0]

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1

        insertAt = 0
        for num in nums:
            if num != 0:
                nums[insertAt] = num
                insertAt += 1

        for i in range(zero_count):
            nums[insertAt] = 0
            insertAt += 1

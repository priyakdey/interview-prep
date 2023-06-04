# https://leetcode.com/problems/maximum-subarray/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max_sum_till = nums[0]
        max_sum_overall = nums[0]

        for i in range(1, len(nums)):
            max_sum_till = max(max_sum_till + nums[i], nums[i])
            max_sum_overall = max(max_sum_overall, max_sum_till)

        return max_sum_overall

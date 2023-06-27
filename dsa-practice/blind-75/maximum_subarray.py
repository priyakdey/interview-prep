# https://leetcode.com/problems/maximum-subarray/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum_at = -1e4 - 1
        max_sum_overall = -1e4 - 1

        for num in nums:
            max_sum_at = max(max_sum_at + num, num)
            max_sum_overall = max(max_sum_overall, max_sum_at)

        return max_sum_overall

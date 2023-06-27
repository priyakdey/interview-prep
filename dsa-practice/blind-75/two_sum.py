# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        pairs = []

        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in seen:
                pairs = [seen[compliment], i]
                break
            seen[num] = i

        return pairs

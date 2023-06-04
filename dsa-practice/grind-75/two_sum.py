# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        indices = []
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in visited:
                indices = [visited[compliment], i]
                break
            visited[num] = i

        return indices

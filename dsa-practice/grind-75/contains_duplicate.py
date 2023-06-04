# https://leetcode.com/problems/contains-duplicate/

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        contains_duplicate = False
        for num in nums:
            if num in seen:
                contains_duplicate = True
                break
            seen.add(num)

        return contains_duplicate

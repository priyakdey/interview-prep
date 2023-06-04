# https://leetcode.com/problems/binary-search/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        index_of = -1
        while start <= end:
            mid = start + (end - start) // 2
            if target == nums[mid]:
                index_of = mid
                break
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

        return index_of

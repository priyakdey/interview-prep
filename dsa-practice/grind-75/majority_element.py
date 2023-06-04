# https://leetcode.com/problems/majority-element/

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        number_frequency_tracker = {}
        majority = None
        for num in nums:
            if num in number_frequency_tracker:
                number_frequency_tracker[num] += 1
            else:
                number_frequency_tracker[num] = 1

            if number_frequency_tracker[num] > len(nums) // 2:
                majority = num
                break

        # cannot be null, since it does exists.
        return majority

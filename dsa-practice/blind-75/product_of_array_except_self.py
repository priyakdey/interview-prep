# https://leetcode.com/problems/product-of-array-except-self/

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums[::-1]

        products = [1 for _ in nums]
        prefix = 1
        postfix = 1

        left = 1
        right = len(nums) - 1 - 1

        while left < len(nums):
            prefix = nums[left - 1] * prefix
            products[left] = products[left] * prefix
            left += 1

            postfix = nums[right + 1] * postfix
            products[right] = products[right] * postfix
            right -= 1

        return products

# https://leetcode.com/problems/product-of-array-except-self/

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return nums[::-1]

        products = [1 for _ in nums]
        left, right = 1, len(nums) - 1 - 1
        prefix_product, postfix_product = 1, 1

        while left < len(nums):
            prefix_product = prefix_product * nums[left - 1]
            products[left] *= prefix_product
            left += 1

            postfix_product = postfix_product * nums[right + 1]
            products[right] *= postfix_product
            right -= 1

        return products

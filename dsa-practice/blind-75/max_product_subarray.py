# https://leetcode.com/problems/maximum-product-subarray/

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max_product_at = nums[0]
        min_product_at = nums[0]
        max_product_overall = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            temp = max(num, max_product_at * num, min_product_at * num)
            min_product_at = min(num, max_product_at * num, min_product_at * num)
            max_product_at = temp

            max_product_overall = max(max_product_overall, max_product_at)

        return max_product_overall

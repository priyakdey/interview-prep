# tag: favourite
# Given an integer array nums, return an array answer such that answer[i] is equal
# to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
#
# You must write an algorithm that runs in O(n) time and without using the
# division operation.
#
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
#
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#
# Constraints:
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# Follow up: Can you solve the problem in O(1) extra space complexity?
# (The output array does not count as extra space for space complexity analysis.)


from typing import List


class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     """This violates the constraint of not using division operator"""
    #     product = 1
    #     zero_count = 0
    #     for num in nums:
    #         if num != 0:
    #             product *= num
    #         else:
    #             zero_count += 1
    #
    #     products = []
    #     for num in nums:
    #         if num != 0:
    #             if zero_count == 0:
    #                 products.append(product // num)
    #             else:
    #                 products.append(0)
    #         else:
    #             if zero_count == 1:
    #                 products.append(product)
    #             else:
    #                 products.append(0)
    #
    #     return products

    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     """This solution does not use the division operator"""

    #     # ith position holds the prefix product of the ith num of nums
    #     # prefix for first element = 1
    #     prefix_products = [1]
    #     # ith position holds the postfix product of the ith num of nums
    #     # postfix for last element = 1
    #     postfix_products = [1]
    #
    #     for i in range(1, len(nums)):
    #         prefix_products.append(nums[i - 1] * prefix_products[-1])
    #
    #     for i in range(len(nums) - 1 - 1, -1, -1):
    #         postfix_products.insert(0, nums[i + 1] * postfix_products[0])
    #
    #     products_array = []
    #     for i in range(len(prefix_products)):
    #         products_array.append(prefix_products[i] * postfix_products[i])
    #
    #     return products_array

    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     """This solution takes the prefix and postfix approach but with O(1) solution"""
    #
    #     products = [1]
    #
    #     # we are calculating the prefix product and pushing to this array
    #     for i in range(1, len(nums)):
    #         products.append(nums[i - 1] * products[-1])
    #
    #     postfix_product = 1
    #     products[-1] = products[-1] * postfix_product
    #
    #     for i in range(len(nums) - 1 - 1, -1, -1):
    #         postfix_product *= nums[i + 1]
    #         products[i] = products[i] * postfix_product
    #
    #     return products

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Try and do this in one pass and with no extra space"""
        if len(nums) == 2:
            return nums[::-1]

        products = [1 for _ in nums]

        prefix_product = 1
        postfix_product = 1
        i, j = 1, len(nums) - 1 - 1

        while i < len(nums):
            # calculate the prefix product for ith member and set products[i]
            prefix_product = nums[i - 1] * prefix_product
            products[i] = products[i] * prefix_product

            # calculate the post product for jth member and set products[j]
            postfix_product = nums[j + 1] * postfix_product
            products[j] = products[j] * postfix_product

            i += 1
            j -= 1

        return products

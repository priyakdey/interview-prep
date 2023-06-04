# tag: favourtite
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
#
# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
#
# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#
# Constraints:
# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length == 3:
            return [nums] if sum(nums) == 0 else []

        def two_sum(value: int, ignore: int) -> List[List[int]]:
            """Returns the indices of two elements which add up to the given target.
            It ignores the `ignore` index.
            Return empty tuple if no such pair found.
            """
            triplets = []
            seen = set()
            for i, num in enumerate(nums):
                if i != ignore:
                    compliment = 0 - value - num
                    if compliment in seen:
                        triplets.append(sorted([compliment, num, value]))
                    else:
                        seen.add(num)

            return triplets

        triplets = []
        seen = set()

        for i, num in enumerate(nums):
            _triplets = two_sum(num, i)
            if len(_triplets) != 0:
                for t in _triplets:
                    if tuple(t) not in seen:
                        triplets.append(t)
                        seen.add(tuple(t))

        return triplets

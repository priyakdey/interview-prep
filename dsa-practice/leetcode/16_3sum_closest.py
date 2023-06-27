# Given an integer array nums of length n and an integer target,
# find three integers in nums such that the sum is closest to target.
#
# Return the sum of the three integers.
#
# You may assume that each input would have exactly one solution.
#
# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
# Example 2:
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
#
# Constraints:
# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104


from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        for i in range(len(nums) - 3 + 1):
            for j in range(i, len(nums) - 2 + 1):
                _target = target - nums[i] - nums[j]
                third = None
                min_diff = 2e4 + 1
                for k in range(j, len(nums) - 1 + 1):
                    if abs(k - min_diff) < min_diff:
                        min_diff = abs(k - min_diff)
                        third = k


soln = Solution()
print(soln.threeSumClosest([1, 2, 5, 6, 7], 4))

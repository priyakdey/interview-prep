# You are given an integer array nums.
# You need to create a 2D array from nums satisfying the following conditions:
#
# The 2D array should contain only the elements of the array nums.
# Each row in the 2D array contains distinct integers.
# The number of rows in the 2D array should be minimal.
# Return the resulting array. If there are multiple answers, return any of them.
#
# Note that the 2D array can have a different number of elements on each row.
#
# Example 1:
# Input: nums = [1,3,4,1,2,3,1]
# Output: [[1,3,4,2],[1,3],[1]]
# Explanation: We can create a 2D array that contains the following rows:
# - 1,3,4,2
# - 1,3
# - 1
# All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
# It can be shown that we cannot have less than 3 rows in a valid array.
#
# Example 2:
# Input: nums = [1,2,3,4]
# Output: [[4,3,2,1]]
# Explanation: All elements of the array are distinct, so we can keep all of them in the first row of the 2D array.
#
#
# Constraints:
# 1 <= nums.length <= 200
# 1 <= nums[i] <= nums.length


from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # get the max
        max_element = max(nums)
        count_arr = [0 for _ in range(max_element + 1)]

        # insert count in the count_array
        for num in nums:
            count_arr[num] += 1

        def is_all_zero(arr: List[int]):
            # count_arr will never have neg int
            return sum(arr) == 0

        mat = []

        while not is_all_zero(count_arr):
            buf = []
            for i in range(len(count_arr)):
                if count_arr[i] != 0:
                    buf.append(i)
                    count_arr[i] -= 1

            mat.append(buf)
            buf = []

        return mat

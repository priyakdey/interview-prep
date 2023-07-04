# Given n non-negative integers representing an elevation map where the
# width of each bar is 1, compute how much water it can trap after raining.
#
# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
#
# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
# Constraints:
# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105


from typing import List


class Solution:
    def trap(self, heights: List[int]) -> int:
        max_height_from_left = []
        max_height = 0
        for height in heights:
            max_height = max(max_height, height)
            max_height_from_left.append(max_height)

        max_height_from_right = []
        max_height = 0
        for i in range(len(heights) - 1, -1, -1):
            max_height = max(max_height, heights[i])
            max_height_from_right.insert(0, max_height)

        vol = 0
        for i, height in enumerate(heights):
            bound = min(max_height_from_left[i], max_height_from_right[i])
            if bound > height:
                vol += (bound - height) * 1

        return vol

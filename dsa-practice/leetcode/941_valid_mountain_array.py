# Given an array of integers arr, return true if and only if it is a valid mountain array.
#
# Recall that arr is a mountain array if and only if:
#
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
#
# Example 1:
# Input: arr = [2,1]
# Output: false
# Example 2:
# Input: arr = [3,5,5]
# Output: false
#
# Example 3:
# Input: arr = [0,3,2,1]
# Output: true
#
# Constraints:
# 1 <= arr.length <= 104
# 0 <= arr[i] <= 104


from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        reached_peak = False
        index = 1
        while not reached_peak and index < len(arr):
            if arr[index] > arr[index - 1]:
                index += 1
                continue
            elif arr[index] == arr[index - 1]:
                return False
            else:
                reached_peak = True

        # peak is at index - 1
        # index is pointing to next element of peak
        if index == 1 or index == len(arr):
            # the first or last element is the peak
            return False

        while index < len(arr):
            if arr[index] < arr[index - 1]:
                index += 1
                continue
            else:
                return False

        return True

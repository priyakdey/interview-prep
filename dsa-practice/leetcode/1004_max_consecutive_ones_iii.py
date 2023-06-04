from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 1 if nums[0] == 1 else 1 if k == 1 else 0

        start, end = 0, 0
        max_length = 0
        flipped = 0
        next_start = 0

        while end < len(nums):
            bit = nums[end]
            if bit == 1:
                if flipped == k:
                    next_start = end
                    print(next_start)
                max_length = max(max_length, end - start + 1)
            else:
                if flipped > k:
                    start = next_start
                    end = start
                    flipped = 0
                else:
                    max_length = max(max_length, end - start + 1)
                    flipped += 1
            end += 1

        return max(max_length, end - start + 1)


soln = Solution()
print(soln.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))

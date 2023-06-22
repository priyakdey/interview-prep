from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_index = []
        for i, num in enumerate(nums):
            if num == 0:
                zero_index.append(i)

        start, end = 0, 0
        zero_count = 0
        max_length = 0
        i = 0
        while end < len(nums):
            num = nums[end]
            if num == 0:
                zero_count += 1
                if zero_count == k + 1:
                    start = zero_index[i] + 1
                    if nums[start] != 0:
                        zero_count -= 1
                    i += 1
            max_length = max(max_length, end - start + 1)
            end += 1

        print(max_length)
        return max_length


if __name__ == "__main__":
    soln = Solution()
    # fmt: off
    assert (soln.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6), "FAILED: 1st case"
    assert (soln.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3) == 10), "FAILED: 2nd case"
    # fmt: on

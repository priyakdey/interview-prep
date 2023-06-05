# https://leetcode.com/problems/3sum/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def two_sum(target: int, ignore: int) -> List[List[int]]:
            visited = {}
            pairs = []
            for i, num in enumerate(nums):
                if i == ignore:
                    continue

                compliment = target - num
                if compliment in visited:
                    pairs.append([compliment, num])

                visited[num] = 1

            return pairs

        triplets = []
        seen = set()

        for i, num in enumerate(nums):
            pairs = two_sum(0 - num, i)
            if len(pairs) != 0:
                for pair in pairs:
                    pair.append(num)
                    pair.sort()
                    if tuple(pair) not in seen:
                        triplets.append(pair)
                        seen.add(tuple(pair))

        return triplets

# https://leetcode.com/problems/top-k-frequent-elements/

import heapq
from typing import List


class Wrapper:
    def __init__(self, num: int, count: int) -> None:
        self.num = num
        self.count = count

    def __eq__(self, node: "Wrapper") -> bool:
        return self.count == node.count

    def __hash__(self, node: "Wrapper") -> bool:
        return self.num

    def __lt__(self, node: "Wrapper") -> bool:
        # this is beacause we are trying to create a max heap
        return self.count > node.count

    def __gt__(self, node: "Wrapper") -> bool:
        # this is beacause we are trying to create a max heap
        return self.count < node.count

    def __str__(self) -> str:
        return f"num = {self.num} and count = {self.count}"

    def __repr__(self) -> str:
        return str(self)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        for num in nums:
            if num in frequency_map:
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1

        heap = []
        for key, value in frequency_map.items():
            heapq.heappush(heap, Wrapper(key, value))

        top_frequent_elements = []
        while k != 0:
            node = heapq.heappop(heap)
            top_frequent_elements.append(node.num)
            k -= 1

        return top_frequent_elements

# You are given two integer arrays nums1 and nums2 sorted in
# ascending order and an integer k.
#
# Define a pair (u, v) which consists of one element from the first array
# and one element from the second array.
#
# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.
#
# Example 1:
# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]]
# Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
#
# Example 2:
# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [[1,1],[1,1]]
# Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
#
# Example 3:
# Input: nums1 = [1,2], nums2 = [3], k = 3
# Output: [[1,3],[2,3]]
# Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
#
# Constraints:
# 1 <= nums1.length, nums2.length <= 105
# -109 <= nums1[i], nums2[i] <= 109
# nums1 and nums2 both are sorted in ascending order.
# 1 <= k <= 104


from typing import Tuple, List


class MinHeap:
    def __init__(self) -> None:
        self.data = []

    def left_child_index(self, parent_index: int) -> int:
        return parent_index * 2 + 1

    def right_child_index(self, parent_index: int) -> int:
        return parent_index * 2 + 2

    def parent_index(self, child_index: int) -> int:
        return (child_index - 1) // 2

    def size(self) -> int:
        return len(self.data)

    def insert(self, num1: int, num2: int) -> None:
        element = (num1, num2, num1 + num2)
        self.data.append(element)

        curr_index = len(self.data) - 1
        parent_index = self.parent_index(curr_index)

        while curr_index > 0 and self.data[curr_index][2] < self.data[parent_index][2]:
            temp = self.data[curr_index]
            self.data[curr_index] = self.data[parent_index]
            self.data[parent_index] = temp
            curr_index = parent_index
            parent_index = self.parent_index(curr_index)

    def extract_min(self) -> Tuple[int, int, int]:
        max_element = self.data[0]

        self.data[0] = self.data[-1]
        self.data = self.data[:-1]

        if len(self.data) > 1:
            curr_index = 0
            while curr_index < len(self.data):
                left_child_index = self.left_child_index(curr_index)
                right_child_index = self.right_child_index(curr_index)

                if left_child_index >= len(self.data):
                    # curr_index is last index, so we can stop
                    break

                swap_index = left_child_index
                if (
                    right_child_index < len(self.data)
                    and self.data[right_child_index][2] < self.data[left_child_index][2]
                ):
                    swap_index = right_child_index

                if self.data[curr_index][2] > self.data[swap_index][2]:
                    temp = self.data[curr_index]
                    self.data[curr_index] = self.data[swap_index]
                    self.data[swap_index] = temp

                curr_index = swap_index

        return max_element

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return str(self.data)


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        heap = MinHeap()
        for num1 in nums1:
            heap.insert(num1, nums2[0])

        pairs = []
        while k != 0 and heap.size() != 0:
            num1, num2, _ = heap.extract_min()
            pairs.append([num1, num2])
            k -= 1

        return pairs


soln = Solution()

assert soln.kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3) == [
    [1, 2],
    [1, 4],
    [1, 6],
], "1st test case failed"
assert soln.kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2) == [
    [1, 1],
    [1, 1],
], "1st test case failed"
assert soln.kSmallestPairs(nums1=[1, 2], nums2=[3], k=3) == [
    [1, 3],
    [2, 3],
], "1st test case failed"

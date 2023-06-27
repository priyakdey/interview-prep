# https://leetcode.com/problems/top-k-frequent-elements/

# import heapq
# from typing import List


# class Wrapper:
#     def __init__(self, num: int, count: int) -> None:
#         self.num = num
#         self.count = count
#
#     def __eq__(self, node: "Wrapper") -> bool:
#         return self.count == node.count
#
#     def __hash__(self, node: "Wrapper") -> bool:
#         return self.num
#
#     def __lt__(self, node: "Wrapper") -> bool:
#         # this is beacause we are trying to create a max heap
#         return self.count > node.count
#
#     def __gt__(self, node: "Wrapper") -> bool:
#         # this is beacause we are trying to create a max heap
#         return self.count < node.count
#
#     def __str__(self) -> str:
#         return f"num = {self.num} and count = {self.count}"
#
#     def __repr__(self) -> str:
#         return str(self)
#
#
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         frequency_map = {}
#         for num in nums:
#             if num in frequency_map:
#                 frequency_map[num] += 1
#             else:
#                 frequency_map[num] = 1
#
#         heap = []
#         for key, value in frequency_map.items():
#             heapq.heappush(heap, Wrapper(key, value))
#
#         top_frequent_elements = []
#         while k != 0:
#             node = heapq.heappop(heap)
#             top_frequent_elements.append(node.num)
#             k -= 1
#
#         return top_frequent_elements


from typing import List


class MaxHeap:
    def __init__(self) -> None:
        self.data = []

    def left_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 1

    def right_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 2

    def parent_index(self, child_index: int) -> int:
        return (child_index - 1) // 2

    def insert(self, num: int) -> None:
        self.data.append(num)

        curr_index = len(self.data) - 1
        parent_index = self.parent_index(curr_index)
        while curr_index > 0 and self.data[curr_index] > self.data[parent_index]:
            temp = self.data[curr_index]
            self.data[curr_index] = self.data[parent_index]
            self.data[parent_index] = temp
            curr_index = parent_index
            parent_index = self.parent_index(curr_index)

    def extract_max(self) -> int:
        max_element = self.data[0]

        self.data[0] = self.data[-1]
        self.data = self.data[:-1]

        if len(self.data) > 1:
            curr_index = 0
            while curr_index < len(self.data):
                left_child_index = self.left_child_index(curr_index)
                right_child_index = self.right_child_index(curr_index)

                if left_child_index >= len(self.data):
                    # curr index == len(self.data) - 1
                    break

                # decide on which child to swap
                swap_index = left_child_index
                if (
                    right_child_index < len(self.data)
                    and self.data[right_child_index] > self.data[left_child_index]
                ):
                    swap_index = right_child_index

                # check if we need to swap the parent
                if self.data[curr_index] < self.data[swap_index]:
                    temp = self.data[curr_index]
                    self.data[curr_index] = self.data[swap_index]
                    self.data[swap_index] = temp
                else:
                    break

                curr_index = swap_index

        return max_element


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        heap = MaxHeap()
        count_array_map = {}

        for num, count in freq_map.items():
            heap.insert(count)
            if count in count_array_map:
                count_array_map[count].append(num)
            else:
                count_array_map[count] = [num]

        top_freq_elements = []

        while k != 0:
            count = heap.extract_max()
            if count in count_array_map:
                value = count_array_map[count]
                top_freq_elements.extend(value)
                del count_array_map[count]
                k -= len(value)

        return top_freq_elements

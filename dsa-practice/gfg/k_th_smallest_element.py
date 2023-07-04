# Given an array arr[] and an integer K where K is smaller than size of array,
# the task is to find the Kth smallest element in the given array.
# It is given that all array elements are distinct.
#
# Note :-  l and r denotes the starting and ending index of the array.
#
# Example 1:
# Input:
# N = 6
# arr[] = 7 10 4 3 20 15
# K = 3
# Output : 7
# Explanation :
# 3rd smallest element in the given
# array is 7.
#
# Example 2:
# Input:
# N = 5
# arr[] = 7 10 4 20 15
# K = 4
# Output : 15
# Explanation :
# 4th smallest element in the given
# array is 15.
#
# Your Task:
# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(log(n))
# Constraints:
# 1 <= N <= 105
# 1 <= arr[i] <= 105
# 1 <= K <= N


class MinHeap:
    """MinHeap can only contain K elements at max at one point of time"""

    def __init__(self) -> None:
        self.data = []

    def left_child_index(self, parent_index: int) -> int:
        return parent_index * 2 + 1

    def right_child_index(self, parent_index: int) -> int:
        return parent_index * 2 + 2

    def parent_index(self, child_index: int) -> int:
        return (child_index - 1) // 2

    def insert(self, v: int) -> None:
        self.data.append(v)

        # heapify the array
        curr_index = len(self.data) - 1
        while curr_index > 0:
            parent_index = self.parent_index(curr_index)
            if self.data[curr_index] < self.data[parent_index]:
                temp = self.data[curr_index]
                self.data[curr_index] = self.data[parent_index]
                self.data[parent_index] = temp

            curr_index = parent_index

    def remove_min(self) -> int:
        min_element = self.data[0]

        # now we heapify
        self.data[0] = self.data[-1]
        self.data = self.data[:-1]

        curr_index = 0
        while curr_index < len(self.data):
            left_child_index = self.left_child_index(curr_index)
            right_child_index = self.right_child_index(curr_index)

            if left_child_index >= len(self.data):
                break

            swap_index = left_child_index
            if (
                right_child_index < len(self.data)
                and self.data[right_child_index] < self.data[left_child_index]
            ):
                swap_index = right_child_index

            if self.data[swap_index] < self.data[curr_index]:
                temp = self.data[swap_index]
                self.data[swap_index] = self.data[curr_index]
                self.data[curr_index] = temp
            else:
                break
            curr_index = swap_index

        return min_element

    def is_empty(self) -> bool:
        return len(self.data) == 0


class Solution:
    def kthSmallest(self, arr, l, r, k):
        """
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        """

        heap = MinHeap()
        for num in arr:
            heap.insert(num)

        min_element = 0
        while k != 0:
            min_element = heap.remove_min()
            k -= 1

        return min_element


soln = Solution()
print(soln.kthSmallest([7, 10, 4, 20, 15], 0, 4, 4))

"""Heap is a ds which has the heap property and is a complete binary tree.
Complete binary tree is one which has all levels filled, except its last level
which might not have all nodes, to make a complete binary tree, we always go
from left to right.
This is why the abstraction is a tree, but this can be backed by an array.

The heap property is a property which makes sure that the parent is smaller
than both its children in case of a min heap. Taking this concept upto the root 
node, this makes the root node as the smallest/min. So extracting min is O(1)
operation.
We can also create a max heap tree, which as the name says has the opposite
property, parents are always greater than its children, making the root node
the max.

The operations we can do on a heap:
1. Insert
2. Delete
3. Heapify
4. Get() -> Extracts the root node - max/min

The calculations are simple, if we look at the array:
index of left child  = 2 * index of parent + 1
index of right child = 2 * index of parent + 2
index of parent      = (child - 1) / 2 
This might not seem obvious with the right child expr, but index cannot be 
fractional, and there can be only parent. So if we check this:
idx(parent) = 4

idx(left) = 2 * 4 + 1 = 9
idx(left) = 2 * 4 + 2 = 10

2 * idx(parent) + 1 = 9
-> idx(parent) = (9 - 1) / 2 = 4

2 * idx(parent) + 2 = 10
-> idx(parent) = (10 - 2) / 2 -> 4.

But we can simply use above formulas to work out the code
"""

from abc import ABC, abstractmethod


class Heap(ABC):
    """Abstract class to represent a Heap."""

    def __init__(self) -> None:
        self.data = []

    @abstractmethod
    def insert(self, num: int) -> None:
        pass

    @abstractmethod
    def extract_root(self) -> int:
        pass

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return self.__str__()

    # private methods. Can be like dunder methods
    def left_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 1

    def right_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 2

    def parent_index(self, child_index: int) -> int:
        return (child_index - 1) // 2


class MaxHeap(Heap):
    def insert(self, num: int) -> None:
        # we just append because new node always go to the last index
        # which guarantees it being complete
        self.data.append(num)

        # now we need to iterate over the nodes and make sure it retains
        # max heap property
        curr_index = len(self.data) - 1
        parent_index = self.parent_index(curr_index)
        while self.data[curr_index] > self.data[parent_index] and curr_index > 0:
            # swap the child and the parent
            temp = self.data[curr_index]
            self.data[curr_index] = self.data[parent_index]
            self.data[parent_index] = temp
            curr_index = parent_index
            parent_index = self.parent_index(curr_index)

    def extract_root(self) -> int:
        """This removes the root and also heapify the heap"""
        # store the root to return at the end of the iteration
        root = self.data[0]

        # copy the last element of the heap to the root
        self.data[0] = self.data[-1]
        # resize so to remove the last element from the heap
        self.data = self.data[:-1]

        if len(self.data) > 1:
            # we need to heapify the tree, top down approach
            curr_index = 0
            while curr_index <= len(self.data) - 1:
                left_child_index = self.left_child_index(curr_index)
                right_child_index = self.right_child_index(curr_index)
                if left_child_index >= len(self.data):
                    # since left always be less, if it is gt than last index, we are out of bounds
                    break

                swap_index = left_child_index
                if (
                    right_child_index < len(self.data)
                    and self.data[right_child_index] > self.data[left_child_index]
                ):
                    swap_index = right_child_index

                if self.data[curr_index] < self.data[swap_index]:
                    temp = self.data[curr_index]
                    self.data[curr_index] = self.data[swap_index]
                    self.data[swap_index] = temp

                curr_index = swap_index

        return root


class MinHeap(Heap):
    def insert(self, num: int) -> None:
        # we just append because new node always go to the last index
        # which guarantees it being complete
        self.data.append(num)

        # now we need to iterate over the nodes and make sure it retains
        # min heap property
        curr_index = len(self.data) - 1
        parent_index = self.parent_index(curr_index)
        while self.data[curr_index] < self.data[parent_index] and curr_index > 0:
            # swap the child and the parent
            temp = self.data[curr_index]
            self.data[curr_index] = self.data[parent_index]
            self.data[parent_index] = temp
            curr_index = parent_index
            parent_index = self.parent_index(curr_index)

    def extract_root(self) -> int:
        root = self.data[0]

        # bring last element to root position and reslice the array
        self.data[0] = self.data[-1]
        self.data = self.data[:-1]

        if len(self.data) > 1:
            # we have more than 1 elements, so we need to heapify
            curr_index = 0
            while curr_index < len(self.data):
                left_child_index = self.left_child_index(curr_index)
                right_child_index = self.right_child_index(curr_index)

                if left_child_index >= len(self.data):
                    # out of bounds, we are the last position
                    break

                swap_index = left_child_index
                if (
                    right_child_index < len(self.data)
                    and self.data[right_child_index] < self.data[left_child_index]
                ):
                    swap_index = right_child_index

                if self.data[curr_index] > self.data[swap_index]:
                    temp = self.data[curr_index]
                    self.data[curr_index] = self.data[swap_index]
                    self.data[swap_index] = temp

                curr_index = swap_index

        return root


# examples of max heap
max_heap = MaxHeap()
nums = [3, 9, 2, 1, 4, 5]
for num in nums:
    max_heap.insert(num)

print("max_heap after all insertions:", max_heap)

for i in range(5):
    print("current root:", max_heap.extract_root())

print("max_heap after all removals:", max_heap)

print("-----------------------------------------")

# examples of min heap
min_heap = MinHeap()
nums = [3, 9, 2, 1, 4, 5]
for num in nums:
    min_heap.insert(num)

print("min_heap after all insertions:", min_heap)

for i in range(2):
    print("current root:", min_heap.extract_root())

print("min_heap after all removals:", min_heap)

# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have
# to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.
#
# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
#
# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
#
# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
#
# Constraints:
#
# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100


from typing import List, Tuple


class Stack:
    def __init__(self) -> int:
        self.data = []

    def push(self, val: int, index: int) -> None:
        self.data.append((val, index))

    def pop(self) -> Tuple[int, int]:
        if self.is_empty():
            raise Exception("Empty Stack")
        return self.data.pop(-1)

    def peek(self) -> Tuple[int, int]:
        return self.data[-1]

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def __str__(self) -> str:
        return str(self.data)


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days_to_wait = [0 for _ in temperatures]

        stack = Stack()

        for index, temp in enumerate(temperatures):
            if stack.is_empty():
                stack.push(temp, index)
            else:
                # check if top is less then curr temp
                if temp > stack.peek()[0]:
                    while not stack.is_empty() and temp > stack.peek()[0]:
                        _, i = stack.pop()
                        days_to_wait[i] = index - i
                stack.push(temp, index)

        return days_to_wait

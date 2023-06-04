# https://leetcode.com/problems/valid-parentheses/


class Stack:
    """Represents a stack data structure"""

    def __init__(self) -> None:
        self.data = []

    def pop(self) -> str:
        if self.is_empty():
            raise Exception("Empty Stack")
        top = self.data[-1]
        del self.data[-1]
        return top

    def push(self, element: str) -> None:
        self.data.append(element)

    def is_empty(self) -> bool:
        return len(self.data) == 0


class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        stack = Stack()
        is_balanced = True
        for parentheses in s:
            if parentheses in parentheses_map:
                if stack.is_empty():
                    is_balanced = False
                    break
                top = stack.pop()
                if top != parentheses_map[parentheses]:
                    is_balanced = False
                    break
            else:
                stack.push(parentheses)

        if is_balanced:
            is_balanced = stack.is_empty()

        return is_balanced

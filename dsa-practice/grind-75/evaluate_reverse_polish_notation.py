# https://leetcode.com/problems/evaluate-reverse-polish-notation/


from typing import List


class Stack:
    def __init__(self) -> None:
        self.data = []
        self.size = 0

    def push(self, value: int) -> None:
        self.data.append(value)
        self.size += 1

    def pop(self) -> int:
        if self.is_empty():
            raise Exception("Stack is empty")
        self.size -= 1
        return self.data.pop(-1)

    def is_empty(self) -> bool:
        return self.size == 0


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = Stack()
        OPERATOR_TOKENS = {"+", "-", "*", "/"}

        def _eval(token: str, a: int, b: int) -> int:
            # fmt: off
            if token == "+": return a + b
            if token == "-": return a - b
            if token == "*": return a * b
            if token == "/": return int(a / b)      # this assumes b != 0
            # fmt: on

        for token in tokens:
            if token in OPERATOR_TOKENS:
                b, a = stack.pop(), stack.pop()
                print(a, token, b)
                stack.push(_eval(token, a, b))
            else:
                stack.push(int(token))

        return stack.pop()

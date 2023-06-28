# tag: favourite
# You are given an array of strings tokens that represents an arithmetic expression
# in a Reverse Polish Notation.
#
# Evaluate the expression. Return an integer that represents the value of the expression.
#
# Note that:
#
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
#
#
# Example 1:
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
#
# Example 2:
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
#
# Example 3:
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
#
# Constraints:
#
# 1 <= tokens.length <= 104
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].


from typing import List


class Stack:
    def __init__(self) -> None:
        self.data = []

    def push(self, val: int) -> None:
        self.data.append(val)

    def pop(self) -> int:
        if self.is_empty():
            raise Exception("Empty stack")
        return self.data.pop(-1)

    def is_empty(self) -> bool:
        return len(self.data) == 0


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """Method evaluates Reverse Polish notation, it does not validate it.
        It is assumed, some client will validate the expr before passing it on
        it this method.

        If expr reached this method, we consider it to be a valid RPN expression
        with valid numeric operators and operands, and not division by zero.
        """

        def eval(a: int, b: int, op: str) -> int:
            if op == "+":
                return a + b
            if op == "-":
                return a - b
            if op == "*":
                return a * b
            # we consider that expression is already validated and hence division by 0 is not a scenario
            if op == "/":
                return int(a / b)

        stack = Stack()

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                b = stack.pop()
                a = stack.pop()
                result = eval(a, b, token)
                stack.push(result)
            else:
                stack.push(int(token))

        return stack.pop()

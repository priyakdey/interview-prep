# Given two binary strings a and b, return their sum as a binary string.
#
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
#
# Constraints:
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.


from typing import Tuple


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def binary_addition(a: str, b: str, c: str) -> Tuple[str]:
            """Returns a tuple of (result, carry) for addition of 3 binary digits"""
            # fmt: off
            if   a == "0" and b == "0" and c == "0": return ("0", "0")
            elif a == "0" and b == "0" and c == "1": return ("1", "0")
            elif a == "0" and b == "1" and c == "0": return ("1", "0")
            elif a == "0" and b == "1" and c == "1": return ("0", "1")
            elif a == "1" and b == "0" and c == "0": return ("1", "0")
            elif a == "1" and b == "1" and c == "0": return ("0", "1")
            elif a == "1" and b == "0" and c == "1": return ("0", "1")
            elif a == "1" and b == "1" and c == "1": return ("1", "1")
            # fmt: on

        i, j = len(a) - 1, len(b) - 1
        carry = "0"
        buffer = []
        while i >= 0 and j >= 0:
            result, carry = binary_addition(a[i], b[j], carry)
            buffer.insert(0, result)
            i -= 1
            j -= 1

        while i >= 0:
            result, carry = binary_addition(a[i], "0", carry)
            buffer.insert(0, result)
            i -= 1

        while j >= 0:
            result, carry = binary_addition("0", b[j], carry)
            buffer.insert(0, result)
            j -= 1

        if carry == "1":
            buffer.insert(0, carry)

        return "".join(buffer)

# https://leetcode.com/problems/add-binary/

from typing import Tuple


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # fmt: off
        def add(a: str, b: str, c: str) -> Tuple[str, str]:
            """Returns in (result, carry) repr"""
            count_one = 0

            if a == "1": count_one += 1
            if b == "1": count_one += 1
            if c == "1": count_one += 1

            if   count_one == 0: return ("0", "0")
            elif count_one == 1: return ("1", "0")
            elif count_one == 2: return ("0", "1")
            else               : return ("1", "1")

        # fmt: off

        
        i, j = len(a) - 1, len(b) - 1
        carry = "0"
        buffer = []
        while i >= 0 and j >= 0:
            result, carry = add(a[i], b[j], carry)
            buffer.insert(0, result)
            i -= 1
            j -=1

        while i >= 0:
            result, carry = add(a[i], "0", carry)
            buffer.insert(0, result)
            i -= 1

        while j >= 0:
            result, carry = add("0", b[j], carry)
            buffer.insert(0, result)
            j -= 1

        if carry == "1":
            buffer.insert(0, "1")

        return "".join(buffer)

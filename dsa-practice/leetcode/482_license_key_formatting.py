# You are given a license key represented as a string s that consists of only
# alphanumeric characters and dashes. The string is separated into n + 1 groups
# by n dashes. You are also given an integer k.
#
# We want to reformat the string s such that each group contains exactly k characters,
# except for the first group, which could be shorter than k but still must contain
# at least one character. Furthermore, there must be a dash inserted between two
# groups, and you should convert all lowercase letters to uppercase.
#
# Return the reformatted license key.
#
# Example 1:
# Input: s = "5F3Z-2e-9-w", k = 4
# Output: "5F3Z-2E9W"
# Explanation: The string s has been split into two parts, each part has 4 characters.
# Note that the two extra dashes are not needed and can be removed.
#
# Example 2:
# Input: s = "2-5g-3-J", k = 2
# Output: "2-5G-3J"
# Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
#
# Constraints:
# 1 <= s.length <= 105
# s consists of English letters, digits, and dashes '-'.
# 1 <= k <= 104


class Stack:
    def __init__(self) -> None:
        self.__data = []

    def push(self, s: str) -> None:
        self.__data.append(s)

    def pop(self) -> str:
        if self.is_empty():
            raise Exception("Stack is empty")

        s = self.__data[-1]
        del self.__data[-1]
        return s

    def is_empty(self) -> bool:
        return len(self.__data) == 0


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        stack = Stack()
        for ch in s:
            if ch != "-":
                stack.push(ch)

        buffer = []
        groups = []

        i = 0
        while not stack.is_empty():
            ch = stack.pop().upper()
            buffer.insert(0, ch)
            i += 1

            if i == k:
                groups.insert(0, "".join(buffer))
                i = 0
                buffer = []

        if len(buffer) != 0:
            groups.insert(0, "".join(buffer))

        return "-".join(groups)

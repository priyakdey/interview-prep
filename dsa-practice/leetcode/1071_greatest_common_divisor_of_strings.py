# tag: favourite
# For two strings s and t, we say "t divides s" if and only if s = t + ... + t
# (i.e., t is concatenated with itself one or more times).
#
# Given two strings str1 and str2, return the largest string x such that x
# divides both str1 and str2.
#
# Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
#
# Example 2:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
#
# Example 3:
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
#
# Constraints:
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.


from typing import List


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == "" or str2 == "":
            return ""

        def split_string_in_parts(s: str, length: int) -> List[str]:
            parts = set()
            buffer = []
            i = 0
            for ch in s:
                if i == length:
                    parts.add("".join(buffer))
                    buffer = [ch]
                    i = 1
                else:
                    buffer.append(ch)
                    i += 1
            else:
                if len(buffer) != 0:
                    parts.add("".join(buffer))

            return list(parts)

        shorter_string, longer_string = str1, str2
        if len(str2) < len(str1):
            shorter_string, longer_string = str2, str1

        for i in range(len(shorter_string), 0, -1):
            substring = shorter_string[:i]
            longer_string_parts = split_string_in_parts(longer_string, len(substring))
            shorter_string_parts = split_string_in_parts(shorter_string, len(substring))

            if len(longer_string_parts) == 1 and len(shorter_string_parts) == 1:
                if longer_string_parts[0] == shorter_string_parts[0]:
                    return longer_string_parts[0]

        return ""

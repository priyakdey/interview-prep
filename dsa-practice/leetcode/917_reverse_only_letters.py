# Given a string s, reverse the string according to the following rules:
#
# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.
#
# Example 1:
# Input: s = "ab-cd"
# Output: "dc-ba"
#
# Example 2:
# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
#
# Example 3:
# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
#
# Constraints:
# 1 <= s.length <= 100
# s consists of characters with ASCII values in the range [33, 122].
# s does not contain '\"' or '\\'.


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # fmt: off
        LETTERS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
        # fmt: on

        buffer = []
        for ch in s:
            buffer.append(ch)

        i, j = 0, len(s) - 1

        while i < j:
            if buffer[i] in LETTERS and buffer[j] in LETTERS:
                temp = buffer[i]
                buffer[i] = buffer[j]
                buffer[j] = temp
                i += 1
                j -= 1
            elif buffer[i] not in LETTERS and buffer[j] in LETTERS:
                i += 1
            elif buffer[i] in LETTERS and buffer[j] not in LETTERS:
                j -= 1
            else:
                i += 1
                j -= 1

        return "".join(buffer)

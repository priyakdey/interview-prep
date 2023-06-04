# Given an integer x, return true if x is a
# palindrome, and false otherwise.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # This uses runs in O(m) where m = number of digits.
        # Uses extra space O(m), but removes any issue of overflow.
        # Can use string conversion, but try and avoid using any std lib conversion
        if x < 0:
            return False

        buffer = []
        while x > 0:
            buffer.append(x % 10)
            x //= 10

        i, j = 0, len(buffer) - 1
        while i < j:
            if buffer[i] != buffer[j]:
                return False
            i += 1
            j -= 1

        return True




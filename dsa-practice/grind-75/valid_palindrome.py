# https://leetcode.com/problems/valid-palindrome/description/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # fmt: off
        valid_letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        # fmt: on

        left, right = 0, len(s) - 1
        is_palindrome = True
        while left < right:
            char_at_left, char_at_right = s[left].lower(), s[right].lower()
            if char_at_left in valid_letters and char_at_right in valid_letters:
                if char_at_left != char_at_right:
                    is_palindrome = False
                    break
                left += 1
                right -= 1
            elif (
                char_at_left not in valid_letters and char_at_right not in valid_letters
            ):
                left += 1
                right -= 1
            elif char_at_left not in valid_letters:
                left += 1
            else:
                right -= 1

        return is_palindrome

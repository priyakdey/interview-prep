# https://leetcode.com/problems/longest-palindrome/


class Solution:
    def longestPalindrome(self, s: str) -> int:
        if s == 1:
            return 1

        if s == 2:
            return 2 if s[0] == s[1] else 1

        letter_count_map = {}
        for ch in s:
            if ch in letter_count_map:
                letter_count_map[ch] += 1
            else:
                letter_count_map[ch] = 1

        odd_count = 0
        maximum_length = 0
        for v in letter_count_map.values():
            maximum_length += v // 2
            if v % 2 != 0:
                odd_count += 1

        # we take v / 2 , so considering element in the one half, double it
        maximum_length *= 2

        if odd_count != 0:
            maximum_length += 1

        return maximum_length

# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length <= 1:
            return length

        if length == 2:
            return 2 if s[0] != s[1] else 1

        max_length = 0
        start, end = 0, 0
        idx_map = {}

        while end < length:
            ch = s[end]
            if ch in idx_map:
                start = max(idx_map[ch] + 1, start)

            max_length = max(max_length, end - start + 1)
            idx_map[ch] = end
            end += 1

        return max_length

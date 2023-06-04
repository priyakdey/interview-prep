# https://leetcode.com/problems/valid-anagram/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count_in_s = {}

        for c in s:
            if c in char_count_in_s:
                char_count_in_s[c] += 1
            else:
                char_count_in_s[c] = 1

        is_anagram = True
        for c in t:
            if c not in char_count_in_s:
                is_anagram = False
                break
            else:
                char_count_in_s[c] -= 1
                if char_count_in_s[c] == 0:
                    del char_count_in_s[c]

        if is_anagram:
            is_anagram = len(char_count_in_s.keys()) == 0

        return is_anagram

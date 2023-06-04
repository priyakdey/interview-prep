# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different
# word or phrase, typically using all the original letters exactly once.
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
#
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#
# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        for c in s:
            if c in s_map:
                s_map[c] = s_map[c] + 1
            else:
                s_map[c] = 1

        for c in t:
            if c in s_map:
                s_map[c] = s_map[c] - 1
                if s_map[c] == 0:
                    del s_map[c]
            else:
                return False

        return True

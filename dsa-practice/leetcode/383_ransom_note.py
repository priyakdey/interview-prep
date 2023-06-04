# Given two strings ransomNote and magazine, return true if ransomNote can be
# constructed by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
#
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
#
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
#
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
#
# Constraints:
# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        magazine_char_count = {}
        for ch in magazine:
            if ch in magazine_char_count:
                magazine_char_count[ch] += 1
            else:
                magazine_char_count[ch] = 1

        for ch in ransomNote:
            if ch in magazine_char_count:
                magazine_char_count[ch] -= 1
                if magazine_char_count[ch] == 0:
                    del magazine_char_count[ch]
            else:
                return False

        return True

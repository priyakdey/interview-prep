# https://leetcode.com/problems/ransom-note/


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False

        magazine_letter_count_map = {}
        for letter in magazine:
            if letter in magazine_letter_count_map:
                magazine_letter_count_map[letter] += 1
            else:
                magazine_letter_count_map[letter] = 1

        can_construct = True
        for letter in ransomNote:
            if letter in magazine_letter_count_map:
                magazine_letter_count_map[letter] -= 1
                if magazine_letter_count_map[letter] == 0:
                    del magazine_letter_count_map[letter]
            else:
                can_construct = False
                break

        return can_construct

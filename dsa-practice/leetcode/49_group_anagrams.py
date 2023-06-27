# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different
# word or phrase, typically using all the original letters exactly once.
#
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Example 2:
# Input: strs = [""]
# Output: [[""]]
#
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
#
# Constraints:
#
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]

        anagram_groups = []

        # groups_map is a map which maps the unique sorted word
        # to a list of its anagram words present in the list.
        # sorted_word acts as the hash here for the words.
        # TODO: maybe we can have a better faster hash algo for actual impl
        groups_map = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in groups_map:
                groups_map[sorted_word].append(word)
            else:
                groups_map[sorted_word] = [word]

        for value in groups_map.values():
            anagram_groups.append(value)

        return anagram_groups

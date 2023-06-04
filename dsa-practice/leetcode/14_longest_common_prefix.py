# Write a function to find the longest common prefix string amongst an array
# of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_common_prefix = ""
        min_length = 201
        for _str in strs:
            _len = len(_str)
            if _len < min_length:
                min_length = _len
                longest_common_prefix = _str

        if min_length == 0:
            # empty string is found, so this has to be the longest common prefix for all
            return ""

        while len(longest_common_prefix) != 0:
            found = True
            for _str in strs:
                if _str[: len(longest_common_prefix)] != longest_common_prefix:
                    found = False
                    break
            if found:
                return longest_common_prefix

            longest_common_prefix = longest_common_prefix[:-1]

        return ""

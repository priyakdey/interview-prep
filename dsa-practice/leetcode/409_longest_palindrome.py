# Given a string s which consists of lowercase or uppercase letters,
# return the length of the longest palindrome that can be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
#
# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
#
# Example 2:
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
#
# Constraints:
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.


class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        for ch in s:
            if ch in char_count:
                char_count[ch] += 1
            else:
                char_count[ch] = 1

        max_length = 0
        is_value_one_value_present = False

        for k, v in char_count.items():
            if v % 2 == 0:
                max_length = max_length + v
            else:
                max_length = max_length + v - 1
                is_value_one_value_present = True

        if is_value_one_value_present:
            # because I can take up one letter from the map in put in the middle (odd length palindrome)
            max_length += 1

        return max_length

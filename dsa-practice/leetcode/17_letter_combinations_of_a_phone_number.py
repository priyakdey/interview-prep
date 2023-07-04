# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. Return the answer in any
# order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.
#
# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
# Example 2:
# Input: digits = ""
# Output: []
#
# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]
#
# Constraints:
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].


from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_to_letter_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        combinations = []
        if len(digits) == 0:
            return combinations

        if len(digits) == 1:
            for c in number_to_letter_map[digits[0]]:
                combinations.append(c)
            return combinations

        def next_combination(combination: str, digits: str) -> None:
            if len(digits) == 0:
                combinations.append(combination)
                return

            for letter in number_to_letter_map[digits[0]]:
                next_combination(combination + letter, digits[1:])

        next_combination("", digits)
        return combinations

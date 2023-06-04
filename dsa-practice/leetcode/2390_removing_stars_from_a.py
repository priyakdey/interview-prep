# You are given a string s, which contains stars *.
#
# In one operation, you can:
#
# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.
#
# Note:
#
# The input will be generated such that the operation is always possible.
# It can be shown that the resulting string will always be unique.
#
#
# Example 1:
# Input: s = "leet**cod*e"
# Output: "lecoe"
# Explanation: Performing the removals from left to right:
# - The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
# - The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
# - The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
# There are no more stars, so we return "lecoe".
#
# Example 2:
# Input: s = "erase*****"
# Output: ""
# Explanation: The entire string is removed, so we return an empty string.
#
#
# Constraints:
# 1 <= s.length <= 105
# s consists of lowercase English letters and stars *.
# The operation above can be performed on s.


# this did not work as this is slow and Time exceeded, so we just take way the abstraction
# class Stack:
#     def __init__(self):
#         self.__table = []
#         self.__cursor = -1

#     def add(self, element: str) -> None:
#         self.__table.append(element)
#         self.__cursor += 1

#     def pop(self) -> Optional[str]:
#         if self.__cursor == -1:
#             return None
#         element = self.__table[-1]
#         self.__table = self.__table[:-1]
#         self.__cursor -= 1
#         return element

#     def is_empty(self) -> bool:
#         return self.__cursor == -1

#     def __repr__(self) -> str:
#         return self.__str__()

#     def __str__(self) -> str:
#         return "".join(self.__table)

# class Solution:
#     def removeStars(self, s: str) -> str:
#         stack = Stack()
#         for ch in s:
#             if ch == "*":
#                 stack.pop()
#             else:
#                 stack.add(ch)

#         return repr(stack)


class Solution:
    def removeStars(self, s: str) -> str:
        buffer = []
        for ch in s:
            if ch == "*":
                if len(buffer) != 0:
                    del buffer[-1]
            else:
                buffer.append(ch)

        return "".join(buffer)

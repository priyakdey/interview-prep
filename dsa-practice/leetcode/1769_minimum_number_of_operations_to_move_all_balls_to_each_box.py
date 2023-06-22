# You have n boxes. You are given a binary string boxes of length n, where boxes[i]
# is '0' if the ith box is empty, and '1' if it contains one ball.
#
# In one operation, you can move one ball from a box to an adjacent box. Box i is
# adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more
# than one ball in some boxes.
#
# Return an array answer of size n, where answer[i] is the minimum number of
# operations needed to move all the balls to the ith box.
#
# Each answer[i] is calculated considering the initial state of the boxes.
#
# Example 1:
# Input: boxes = "110"
# Output: [1,1,3]
# Explanation: The answer for each box is as follows:
# 1) First box: you will have to move one ball from the second box to the first box in one operation.
# 2) Second box: you will have to move one ball from the first box to the second box in one operation.
# 3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.
#
# Example 2:
# Input: boxes = "001011"
# Output: [11,8,5,4,3,4]
#
# Constraints:
# n == boxes.length
# 1 <= n <= 2000
# boxes[i] is either '0' or '1'.


from typing import List


class Solution:
    # def minOperations(self, boxes: str) -> List[int]:
    #     number_of_moves_array = []
    #     for i in range(len(boxes)):
    #         number_of_moves = 0
    #         for j, n in enumerate(boxes):
    #             if i != j:
    #                 number_of_moves += int(n) * abs(j - i)
    #         number_of_moves_array.append(number_of_moves)
    #
    #     return number_of_moves_array

    def minOperations(self, boxes: str) -> List[int]:
        left = []
        right = []

        for i in range(1, len(boxes)):
            if boxes[i] != "0":
                right.append(i)

        output = []

        print(left, right)

        output.append(sum(left) + sum(right))

        for i in range(1, len(boxes)):
            if boxes[i - 1] == "1":
                left.append(i - 1)

            # modify right
            if boxes[i] == "1":
                right = right[1:]

            left_distance = sum(map(lambda x: abs(x - i), left))
            right_distance = sum(map(lambda x: abs(x - i), right))

            output.append(left_distance + right_distance)

        return output

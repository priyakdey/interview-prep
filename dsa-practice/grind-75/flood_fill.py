# https://leetcode.com/problems/flood-fill/

from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        starting_color = image[sr][sc]

        rows, cols = len(image), len(image[0])

        def colorize(x: int, y: int) -> None:
            if x < 0 or x >= rows:
                return

            if y < 0 or y >= cols:
                return

            if image[x][y] != starting_color:
                return

            # fill the color
            image[x][y] = color

            colorize(x - 1, y)  # above cell
            colorize(x + 1, y)  # bottom cell
            colorize(x, y - 1)  # left cell
            colorize(x, y + 1)  # right cell

        colorize(sr, sc)
        return image

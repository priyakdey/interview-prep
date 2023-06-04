# tag: favourite
# An image is represented by an m x n integer grid image where image[i][j]
# represents the pixel value of the image.

# You are also given three integers sr, sc, and color.
# You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected
# 4-directionally to the starting pixel of the same color as the starting pixel,
# plus any pixels connected 4-directionally to those pixels (also with the same color),
# and so on. Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.


from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        starting_color = image[sr][sc]

        def flood_fill(x: int, y: int) -> None:
            if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]):
                return

            if image[x][y] != starting_color or image[x][y] == color:
                return

            image[x][y] = color

            flood_fill(x - 1, y)  # cell above
            flood_fill(x + 1, y)  # cell below
            flood_fill(x, y - 1)  # cell left
            flood_fill(x, y + 1)  # cell right

        flood_fill(sr, sc)
        return image

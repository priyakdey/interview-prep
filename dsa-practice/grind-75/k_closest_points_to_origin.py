# https://leetcode.com/problems/k-closest-points-to-origin/

import math
import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Dict[int -> List[List[int]]]
        distance_to_points_map = {}
        distances = []
        for point in points:
            distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
            heapq.heappush(distances, distance)
            if distance in distance_to_points_map:
                distance_to_points_map[distance].append(point)
            else:
                distance_to_points_map[distance] = [point]

        closest_points = []
        while k != 0:
            distance = heapq.heappop(distances)
            points = distance_to_points_map[distance]
            closest_points.extend(points)
            k -= len(points)

        return closest_points

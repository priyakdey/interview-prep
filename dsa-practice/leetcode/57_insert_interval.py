# tag: favourites
# You are given an array of non-overlapping intervals intervals where
# intervals[i] = [starti, endi] represent the start and the end of the ith interval
# and intervals is sorted in ascending order by starti.
# You are also given an interval newInterval = [start, end] that represents the
# start and end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in
# ascending order by starti and intervals still does not have any overlapping
# intervals (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.
#
# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
#
# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
#
# Constraints:
# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 105
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 105


from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # Step1. Do a binary seach to get the insertion position of this interval
        # Step2. Iterate over the new list and merge them accordingly

        start, end = 0, len(intervals) - 1
        insertAt = 0

        while start <= end:
            mid = start + (end - start) // 2
            if newInterval[0] == intervals[mid][0]:
                if newInterval[1] >= intervals[mid][1]:
                    insertAt = mid + 1
                else:
                    insertAt = mid
                break

            if newInterval[0] > intervals[mid][0]:
                if mid == len(intervals) - 1:
                    insertAt = len(intervals)
                    break
                if newInterval[0] < intervals[mid + 1][0]:
                    insertAt = mid + 1
                    break
                else:
                    start = mid + 1
            else:
                if mid == 0:
                    insertAt = 0
                    break
                if newInterval[0] > intervals[mid - 1][0]:
                    insertAt = mid
                    break
                else:
                    end = mid - 1

        intervals.insert(insertAt, newInterval)

        print(intervals)

        merged_intervals = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] > merged_intervals[-1][1]:
                merged_intervals.append(intervals[i])
            elif intervals[i][0] < merged_intervals[-1][1]:
                start = min(intervals[i][0], merged_intervals[-1][0])
                end = max(intervals[i][1], merged_intervals[-1][1])
                merged_intervals[-1] = [start, end]
            else:
                merged_intervals[-1] = [merged_intervals[-1][0], intervals[i][1]]

        return merged_intervals

import time


class Solution:
    def minJumps(self, arr, n):
        start = 0
        end = 1
        number_of_jumps = 0

        while end < len(arr):
            # time.sleep(2)
            next_start = end

            next_start = arr[max(arr[start:end])]
            start = next_start
            end = start + 1
            print(start, end)
            number_of_jumps += 1

        return number_of_jumps


arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
soln = Solution()
print(soln.minJumps(arr, len(arr)))

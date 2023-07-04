class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()

        min_diff = arr[-1] - arr[0]

        if arr[-1] - k > 0:
            for i in range(n - 2 + 1):
                if arr[i + 1] - k < 0:
                    continue
                smallest = min(arr[0] + k, arr[i + 1] - k)
                highest = max(arr[i] + k, arr[-1] - k)
                min_diff = min(min_diff, highest - smallest)
                print(arr, i, smallest, highest, min_diff)

        return min_diff


soln = Solution()
print(soln.getMinDiff([2, 6, 3, 4, 7, 2, 10, 3, 2, 1], 10, 5))
print(soln.getMinDiff([1, 9, 10, 1, 1, 3, 10, 3, 4, 6], 10, 4))

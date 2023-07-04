class Solution:
    def sort012(self, arr, n):
        count_array = [0, 0, 0]
        for num in arr:
            count_array[num] += 1

        cursor = 0
        for i in range(cursor, count_array[0]):
            arr[i] = 0

        cursor += count_array[0]
        for i in range(cursor, cursor + count_array[1]):
            arr[i] = 1

        cursor += count_array[1]
        for i in range(cursor, cursor + count_array[2]):
            arr[i] = 2


soln = Solution()
arr = [0, 2, 1, 2, 0]
soln.sort012(arr, len(arr))
print(arr)

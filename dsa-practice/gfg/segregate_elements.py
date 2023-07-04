class Solution:
    def segregateElements(self, arr, n):
        temp = []
        for num in arr:
            if num >= 0:
                temp.append(num)

        for num in arr:
            if num < 0:
                temp.append(num)

        for i, num in enumerate(temp):
            arr[i] = num

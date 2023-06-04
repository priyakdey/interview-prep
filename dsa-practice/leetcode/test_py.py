class Solution:
    # Function to find the days of buying and selling stock for max profit.
    def stockBuySell(self, A, n):
        profit = []
        max_price = A[0]

        max_price_index = 0
        buying_price_index = 0

        for i in range(1, n):
            price = A[i]
            if price < max_price:
                profit.append([buying_price_index, max_price_index])
                buying_price_index = i

            max_price = price
            max_price_index = i

        if buying_price_index != max_price_index:
            profit.append([buying_price_index, max_price_index])

        return profit


# fmt: off

soln = Solution()

nums = [4, 3, 2, 1]

print(nums)

print(soln.stockBuySell(nums, len(nums)))


# fmt: on

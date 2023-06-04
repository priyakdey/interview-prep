# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        minimum_price_till_date = prices[0]
        maximum_profit = 0

        for i in range(1, len(prices)):
            curr_price = prices[i]
            minimum_price_till_date = min(minimum_price_till_date, curr_price)
            maximum_profit = max(maximum_profit, curr_price - minimum_price_till_date)

        return maximum_profit

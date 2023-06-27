# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buying_price = prices[0]

        for price in prices:
            buying_price = min(buying_price, price)
            max_profit = max(max_profit, price - buying_price)

        return max_profit

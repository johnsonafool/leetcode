from typing import List
import math


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy at lowest
        buy = math.inf
        ans = 0
        for price in prices:
            profit = price - buy
            ans = max(ans, profit)
            buy = min(buy, price)
        return ans


sol = Solution()

print(sol.maxProfit(prices=[3, 2, 6, 5, 0, 3]))

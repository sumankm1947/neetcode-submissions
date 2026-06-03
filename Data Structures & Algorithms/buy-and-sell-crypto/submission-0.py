class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        stack = prices[0]
        for price in prices:
            if price > stack:
                profit = price - stack
                ans = max(profit, ans)
            elif price < stack:
                stack = price
        
        return ans
            
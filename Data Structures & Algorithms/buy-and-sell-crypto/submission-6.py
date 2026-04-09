class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, res = 0, 1, 0 

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                res = max(res, profit)
            else: 
                left = right
            right += 1

        return res  
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left = buy day, right = sell day
        left, right = 0, 1 
        res = 0 

        while right < len(prices):
            # If profitable, calculate profit and update our max record
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                res = max(res, profit)
            else:
                # If the right price is LOWER than our left price, 
                # we found a new cheapest day to buy. Move left to right.
                left = right
            
            # Always move the right pointer to explore the next selling day
            right += 1
            
        return res
        
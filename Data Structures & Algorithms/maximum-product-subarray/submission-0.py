# DP Type: Bottom-Up Dynamic Programming (Space-Optimized Tabulation)

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = nums[0]
        curMax, curMin = 1, 1
        
        for n in nums:
            if n < 0:
                curMax, curMin = curMin, curMax
            
            curMax = max(n, n * curMax)
            curMin = min(n, n * curMin)
            res = max(res, curMax)
            
        return res
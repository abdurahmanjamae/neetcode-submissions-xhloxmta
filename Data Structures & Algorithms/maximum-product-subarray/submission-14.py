class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMax, currMin = 1,1

        for n in nums:
            if n < 0:
                currMax, currMin = currMin, currMax
            
            currMax = max(n, n * currMax)
            currMin = min(n, n * currMin)
            res = max(res, currMax)
        return res
        
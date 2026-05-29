# DP Type: Bottom-Up Dynamic Programming (Space-Optimized Tabulation)

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # Global result tracker initialized to the first number
        res = nums[0]
        
        # Track the running maximum and minimum products ending at the current position
        curMax, curMin = 1, 1
        
        for n in nums:
            # If we hit a negative number, its multiplication flips the max to min and min to max.
            # Swapping them upfront simplifies our math.
            if n < 0:
                curMax, curMin = curMin, curMax
            
            # # Calculate max/min by either starting a new subarray at n, or extending the existing product chain
            curMax = max(n, n * curMax)
            # The new curMin tracks the most negative bound
            curMin = min(n, n * curMin)
            
            # Update our global maximum result
            res = max(res, curMax)
            
        return res

# Time Complexity: O(n)
# We loop through the array exactly once, performing constant time comparisons.

# Space Complexity: O(1)
# We only use a few scalar variables, completely eliminating any DP array memory footprint.
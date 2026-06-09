# DP Type: Bottom-Up Dynamic Programming (Space-Optimized Tabulation / Kadane's Algorithm)

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = nums[0]
        currSum = 0

        for n in nums:
            # If the rolling sum drops below zero, discard it completely
            if currSum < 0:
                currSum = 0
            
            # Add the current number to our running window sum
            currSum += n
            # Track the peak sum seen at any point
            maxSum = max(maxSum, currSum)
        
        return maxSum

# Time Complexity: O(n) -> We loop through the array exactly once.
# Space Complexity: O(1) -> We only use two scalar variables (maxSum, currSum).
# DP Type: Bottom-Up Dynamic Programming (Space-Optimized Tabulation / Kadane's Algorithm)

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Initialize global max and current running max with the first element
        max_sum = nums[0]
        current_sum = nums[0]
        
        # Iterate through the rest of the array starting at index 1
        for n in nums[1:]:
            # Decide whether to add n to the existing subarray or start a new subarray at n
            current_sum = max(n, current_sum + n)
            
            # Update our global maximum if the current subarray sum is larger
            max_sum = max(max_sum, current_sum)
            
        return max_sum

# Time Complexity: O(n)
# We loop through the array exactly once, performing constant time checks.

# Space Complexity: O(1)
# We optimize away the DP array completely by tracking sums using only two variables.

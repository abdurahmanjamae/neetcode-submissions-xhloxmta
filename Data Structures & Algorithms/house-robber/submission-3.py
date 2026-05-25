# DP Type: Bottom-Up Dynamic Programming (Tabulation)

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # Base cases: If only 1 or 2 houses exist, return the max value possible immediately
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        # Initialize DP table to store the maximum money stolen up to house i
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Iteratively fill the table by choosing to rob the current house (plus loot from i-2) or skip it
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        # The last element holds the maximum total amount that can be stolen safely
        return dp[n-1]

# Time Complexity: O(n)
# We iterate through the list of houses exactly once in a single linear loop.

# Space Complexity: O(n)
# Required to store the maximum loot subproblems in the `dp` array of length n.
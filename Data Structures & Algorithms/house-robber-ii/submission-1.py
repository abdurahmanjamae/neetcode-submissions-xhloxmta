# DP Type: Bottom-Up Dynamic Programming (Tabulation) with Array Slicing

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # Base case: if there's only 1 house, it cannot loop back to itself
        if n == 1:
            return nums[0]

        # Break circular constraint by comparing two linear streets: skip first house vs skip last house.
        # nums[1:] ignores the 1st house, making it safe to consider robbing the last house.
        # nums[:-1] ignores the last house, making it safe to consider robbing the 1st house.
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums: List[int]) -> int:
        n = len(nums)

        # Match your original House Robber 1 base cases exactly
        if n == 1:
            return nums[0]
        if n == 2: 
            return max(nums[0], nums[1])

        # Match your exact House Robber 1 DP array initialization
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Match your exact House Robber 1 loop and relation step
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[n-1]

# Time Complexity: O(n)
# We traverse through the sliced arrays sequentially in linear time.

# Space Complexity: O(n)
# Required to allocate space for the sliced arrays and the internal DP tables.
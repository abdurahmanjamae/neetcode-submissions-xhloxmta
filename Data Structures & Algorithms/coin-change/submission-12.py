# DP Type: 1D Bottom-Up Dynamic Programming (Tabulation)

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Initialize DP table filled with a value greater than any possible coin count
        # (amount + 1 acts as our conceptual "infinity")
        dp = [amount + 1] * (amount + 1)
        
        # Base case: 0 coins are needed to make an amount of 0
        dp[0] = 0
        
        # Compute the minimum coins needed for every small amount up to the target
        for i in range(1, amount + 1):
            for coin in coins:
                # Only use the coin if it doesn't exceed the current subproblem amount
                if i - coin >= 0:
                    # State transition: min(current value, 1 + value of remaining amount)
                    dp[i] = min(dp[i], 1 + dp[i - coin])
                    
        # If the target amount cell was never updated, it means it's impossible
        return dp[amount] if dp[amount] != amount + 1 else -1

# Time Complexity: O(n*t)
# We run a nested loop through every amount up to the target, checking every coin option.
# Where n is the length of the array coing and t is the given amount

# Space Complexity: O(t)
# Required to store our 1D DP array of size amount + 1.
# DP/Greedy Type: Bottom-Up Bitwise Dynamic Programming (Subproblem Overlap)
# General Greedy Definition: An algorithmic paradigm that builds up a solution piece 
# by piece, always making the choice that seems best at that exact moment (locally optimal), 
# without worrying about the future impact. It hopes that these local choices lead 
# to a globally optimal solution.

class Solution:
    def countBits(self, n: int) -> list[int]:
        # Initialize DP table filled with zeros up to size n
        dp = [0] * (n + 1)
        
        # Build the solution for each number sequentially from 1 to n
        for i in range(1, n + 1):
            # The number of 1 bits in 'i' is equal to 1 plus the number of 1 bits 
            # in the number obtained by clearing i's lowest set bit.
            dp[i] = dp[i & (i - 1)] + 1
            
        return dp

# Time Complexity: O(n) -> We compute the bit count for each number in exactly O(1) constant time.
# Space Complexity: O(n) -> The memory space required to hold the returned DP array of size n + 1.
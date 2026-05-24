# DP Type: Top-Down Dynamic Programming (Memoization)

class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases: 1 step has 1 way, 2 steps have 2 ways
        memo = {1:1, 2:2}

        def f(n):
            # Return cached result if already calculated
            if n in memo:
                return memo[n]
            # Calculate current steps by adding subproblem results and cache it
            else:
                memo[n] = f(n-2) + f(n-1)
                return memo[n]
                
        return f(n)

# Time Complexity: O(n)
# Each value from 3 to n is computed exactly once due to memoization.

# Space Complexity: O(n)
# Required for the recursion stack and the memoization hash map size.
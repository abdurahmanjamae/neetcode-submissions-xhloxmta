# DP Type: 2D Bottom-Up Dynamic Programming (Tabulation)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D grid with padded out-of-bound rows/cols initialized to 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base case: There is exactly 1 way to reach the destination from itself
        dp[m - 1][n - 1] = 1

        # Iterate backward through the grid rows and columns
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Skip the destination cell to preserve our base case of 1
                if i == m - 1 and j == n - 1:
                    continue
                # Paths from current cell = paths from cell below + paths from cell to the right
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        # The top-left cell stores the total unique paths for the entire grid
        return dp[0][0]

# Time Complexity: O(m * n)
# We traverse every single cell in the m x n grid exactly once.

# Space Complexity: O(m * n)
# Required for our 2D grid table of size (m + 1) * (n + 1).
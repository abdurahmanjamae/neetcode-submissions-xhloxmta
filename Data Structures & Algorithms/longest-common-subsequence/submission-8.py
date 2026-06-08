# DP Type: 2D Bottom-Up Dynamic Programming (Tabulation)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Initialize a 2D grid with an extra row and column of 0s for base cases
        dp = [[0 for j in range(len(text2) + 1)]
                 for i in range(len(text1) + 1)]

        # Iterate backward through both strings
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # If characters match, take the diagonal value and add 1
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                # If they mismatch, take the max from the right or bottom neighbor
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        # Top-left cell contains the LIS for both full strings
        return dp[0][0]

# Time Complexity: O(n * m)
# Where n is len(text1) and m is len(text2). We iterate through every cell of the grid.

# Space Complexity: O(n * m)
# Required for the 2D DP matrix table of size (n + 1) * (m + 1).
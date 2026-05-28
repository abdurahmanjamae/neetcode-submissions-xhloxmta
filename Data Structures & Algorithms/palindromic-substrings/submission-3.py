# DP Type: Bottom-Up Dynamic Programming (Tabulation) Matrix

class Solution:
    def countSubstrings(self, s: str) -> int:
        n, res = len(s), 0
        
        # Initialize an n x n grid where dp[i][j] signifies if s[i:j+1] is a palindrome
        dp = [[False] * n for _ in range(n)]

        # Walk i backwards and j forwards to resolve inner subproblems before outer ones
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                # Condition: End characters match and the inner substring is valid (or string length <= 3)
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    res += 1 # Increment total count for every true palindrome found
                    
        return res

# Time Complexity: O(n²)
# We check every unique substring window combination exactly once.

# Space Complexity: O(n²)
# Required for the n x n matrix lookup table.
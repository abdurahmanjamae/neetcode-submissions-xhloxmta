# DP Type: Bottom-Up Dynamic Programming (Tabulation) Matrix

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Track the starting index and length of the best palindrome found
        resIdx, resLen = 0, 0
        n = len(s)

        # Initialize a 2D matrix where dp[i][j] signifies if s[i:j+1] is a palindrome
        dp = [[False] * n for _ in range(n)]

        # Walk i backwards and j forwards to resolve inner subproblems before outer ones
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                # Condition: End characters must match, AND either the string is short 
                # (length <= 3, meaning j - i <= 2) OR the inner substring is a confirmed palindrome.
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    
                    # If this current palindrome window is the longest seen, save it
                    if resLen < (j - i + 1):
                        resIdx = i
                        resLen = j - i + 1

        # Slice out and return the longest palindromic substring
        return s[resIdx : resIdx + resLen]

# Time Complexity: O(n²)
# We visit each unique state (i, j) in the upper triangle of our matrix exactly once.

# Space Complexity: O(n²)
# Required to maintain the n x n matrix table grid for storing look-behind truths.
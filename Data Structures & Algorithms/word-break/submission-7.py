# DP Type: Bottom-Up Dynamic Programming (Tabulation)

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # dp[i] will store whether s[i:] can be segmented into valid words
        dp = [False] * (len(s) + 1)
        # Base case: An empty suffix at the very end is a valid segmentation
        dp[len(s)] = True

        # Outer loop walks backward through the string positions
        for i in range(len(s) - 1, -1, -1):
            for j in wordDict:
                # If the word fits within bounds and matches the current substring slice
                if (i + len(j)) <= len(s) and s[i : i + len(j)] == j:
                    # Inherit the truth value of the remaining string following this word
                    dp[i] = dp[i + len(j)]
                
                # Optimization: If we found a valid path for dp[i], stop checking other words
                if dp[i]:
                    break
                    
        return dp[0]

# Time Complexity: O(n * m * k)
# Where n is len(s), m is len(wordDict), and k is the average length of the words (due to string slicing).

# Space Complexity: O(n)
# Required for our 1D DP array of size n + 1.
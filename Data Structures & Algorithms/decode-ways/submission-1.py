# DP Type: 1D Bottom-Up Dynamic Programming (Tabulation)

class Solution:
    def numDecodings(self, s: str) -> int:
        # Return 0 if the string is empty or starts with an invalid '0' (can't be decoded)
        if not s or s[0] == "0":
            return 0
            
        n = len(s)
        # dp[i] stores the number of ways to decode the string up to length i
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1  # An empty string has 1 valid way to be decoded (doing nothing)
        dp[1] = 1  # A single non-zero digit has 1 valid way
        
        for i in range(2, n + 1):
            # Check 1-digit jump (look at previous character)
            one_digit = int(s[i-1 : i])
            if 1 <= one_digit <= 9:
                dp[i] += dp[i-1]
                
            # Check 2-digit jump (look at previous two characters)
            two_digits = int(s[i-2 : i])
            if 10 <= two_digits <= 26:
                dp[i] += dp[i-2]
                
        return dp[n]

# Time Complexity: O(n)
# We loop through the string exactly once, doing constant time math at each step.

# Space Complexity: O(n)
# Required for our 1D DP array of size n + 1.
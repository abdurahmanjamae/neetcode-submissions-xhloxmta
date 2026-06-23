# DP/Greedy Type: Bit Manipulation (Brian Kernighan's Bit-Clearing)
# General Greedy Definition: An algorithmic paradigm that builds up a solution piece 
# by piece, always making the choice that seems best at that exact moment (locally optimal), 
# without worrying about the future impact. It hopes that these local choices lead 
# to a globally optimal solution.

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        # Process until all set bits are cleared to zero
        while n > 0:
            # This bitwise operation clears the lowest set '1' bit to '0'
            n = n & (n - 1)
            count += 1
            
        return count

# Time Complexity: O(k) -> Where k is the number of 1 bits present (at most 32 operations).
# Space Complexity: O(1) -> Runs entirely in-place with a single counter variable.
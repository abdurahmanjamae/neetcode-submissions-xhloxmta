# DP/Greedy Type: Bitwise Reversal Simulation (Bit-Shifting Pipeline)
# General Greedy Definition: An algorithmic paradigm that builds up a solution piece 
# by piece, always making the choice that seems best at that exact moment (locally optimal), 
# without worrying about the future impact. It hopes that these local choices lead 
# to a globally optimal solution.

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        # We must iterate exactly 32 times because it is a fixed 32-bit integer
        for i in range(32):
            # 1. Shift the result left to make space for the next bit
            res <<= 1
            
            # 2. (n & 1) grabs the last bit of n; |= inserts it into our shifted result
            res |= (n & 1)
            
            # 3. Shift n right to move the next bit into the lowest position
            n >>= 1
            
        return res

# Time Complexity: O(1) -> The loop always runs exactly 32 times, ensuring constant time.
# Space Complexity: O(1) -> Run completely in-place using only integer references.
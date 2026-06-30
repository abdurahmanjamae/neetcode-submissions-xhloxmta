# DP/Greedy Type: Bitwise Hardware Simulation (Half-Adder Pipeline)
# General Greedy Definition: An algorithmic paradigm that builds up a solution piece 
# by piece, always making the choice that seems best at that exact moment (locally optimal), 
# without worrying about the future impact. It hopes that these local choices lead 
# to a globally optimal solution.

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask to handle Python's infinite integer precision
        mask = 0xFFFFFFFF
        
        # Loop until there are no remaining carries to add
        while b != 0:
            # 1. Calculate the raw sum without carries using XOR, then clamp to 32-bit
            sum_without_carry = (a ^ b) & mask
            
            # 2. Find common set bits using AND, then shift left to create the carry bits
            carry = ((a & b) << 1) & mask
            
            # 3. Update variables for the next round of addition
            a = sum_without_carry
            b = carry
            
        # If 'a' is a negative 32-bit number, format it correctly for Python
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)

# Time Complexity: O(1) -> The loop runs at most 32 times because carries shift out of bounds.
# Space Complexity: O(1) -> Performed in-place with integer variables.
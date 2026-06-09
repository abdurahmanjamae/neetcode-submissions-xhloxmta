# DP/Greedy Type: Backward Greedy Target Shift (Space-Optimized)
# General Greedy Definition: An algorithmic paradigm that builds up a solution piece 
# by piece, always making the choice that seems best at that exact moment (locally optimal), 
# without worrying about the future impact. It hopes that these local choices lead 
# to a globally optimal solution.

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # Get the total number of elements in the array to establish grid bounds
        n = len(nums)
        # Start our target at the final destination index
        target = n - 1

        # Walk backward through the array from right to left
        for i in range(n - 1, -1, -1):
            maxJump = nums[i]
            # If we can reach or pass the current target from index i
            if i + maxJump >= target:
                # Move the target closer to the start line
                target = i
        
        # If the target reached index 0, a complete valid path exists
        return target == 0

# Time Complexity: O(n) -> We scan the array of length n exactly once.
# Space Complexity: O(1) -> We only track a couple of integer variables.
# DP/Greedy Type: Backward Greedy Target Shift (Space-Optimized)
# Greedy Strategy: Instead of calculating every single jump path combination, we make 
# the locally optimal choice at each step by shifting our goalpost ("target") to the 
# closest possible index that can reach the end.

class Solution:
    def canJump(self, nums: list[int]) -> bool:
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
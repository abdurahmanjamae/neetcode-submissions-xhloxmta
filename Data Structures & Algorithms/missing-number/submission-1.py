# DP/Greedy Type: Running Difference Accumulation (Linear Math Balancer)
# General Greedy Definition: An algorithmic paradigm that builds up a solution piece 
# by piece, always making the choice that seems best at that exact moment (locally optimal), 
# without worrying about the future impact. It hopes that these local choices lead 
# to a globally optimal solution.

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # Initialize res with len(nums) because the loop index i only goes up to len(nums) - 1
        res = len(nums)
        
        # Track the running difference between expected index and actual value
        for i in range(len(nums)):
            res += (i - nums[i])
            
        return res

# Time Complexity: O(n) -> A single linear pass through the array.
# Space Complexity: O(1) -> Runs entirely in-place with a single counter.
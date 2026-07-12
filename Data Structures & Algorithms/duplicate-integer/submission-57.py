# DP/Greedy Type: Hash Set Tracking (Early Return Search)
# General Greedy Definition: An algorithmic paradigm that builds up a solution piece 
# by piece, always making the choice that seems best at that exact moment (locally optimal), 
# without worrying about the future impact. It hopes that these local choices lead 
# to a globally optimal solution.

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        # Create an empty hash set to keep track of numbers we have already evaluated
        seen = set()

        for num in nums:
            # If the current number is already in our set, we found a duplicate
            if num in seen:
                return True
            # Otherwise, record this number in the set and keep moving
            else:
                seen.add(num)
                
        # If the loop finishes without finding any matches, all numbers are unique
        return False

# Time Complexity: O(n) -> A single linear pass through the array, with O(1) set lookups.
# Space Complexity: O(n) -> In the worst-case scenario, the set stores every element.
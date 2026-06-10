# DP/Greedy Type: Linear Greedy Scanning (One-Pass)
# General Greedy Definition: An algorithmic paradigm that builds up a solution piece 
# by piece, always making the choice that seems best at that exact moment (locally optimal), 
# without worrying about the future impact. It hopes that these local choices lead 
# to a globally optimal solution.

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        
        for slot in intervals:
            # Case 1: Current interval is completely before the new interval
            if slot[1] < newInterval[0]:
                res.append(slot)
            
            # Case 2: Current interval is completely after the new interval
            elif slot[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = slot  # Shift pointer so the remaining intervals slide in smoothly
            
            # Case 3: Overlap occurs, merge intervals greedily
            else:
                newInterval[0] = min(newInterval[0], slot[0])
                newInterval[1] = max(newInterval[1], slot[1])
        
        # Append the final remaining tracked interval
        res.append(newInterval)
        return res

# Time Complexity: O(n) -> We process the array of n intervals exactly once.
# Space Complexity: O(n) -> Required to store and return the new result list.
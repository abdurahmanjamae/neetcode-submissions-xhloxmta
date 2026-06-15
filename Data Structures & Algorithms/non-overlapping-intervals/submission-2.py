# DP/Greedy Type: Sort by End Time & Linear Scan (One-Pass)
# General Greedy Definition: An algorithmic paradigm that builds up a solution piece 
# by piece, always making the choice that seems best at that exact moment (locally optimal), 
# without worrying about the future impact. It hopes that these local choices lead 
# to a globally optimal solution.

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # Crucial Greedy Step: Sort intervals by their END times i[1]
        intervals.sort(key=lambda i: i[1])
        
        # Track the end time of the last accepted non-overlapping interval
        prevEnd = intervals[0][1]
        res = 0
        
        # Loop through the remaining intervals starting at index 1
        for i in intervals[1:]:
            # If the current interval starts before the previous one ends, they overlap
            if i[0] < prevEnd:
                res += 1  # Greedily remove the current interval
            else:
                # No overlap! Update our boundary marker to the current interval's end
                prevEnd = i[1]
                
        return res

# Time Complexity: O(n log n) -> Driven entirely by the sorting step. 
# Space Complexity: O(n) -> Internal memory required for Python's sorting algorithm.
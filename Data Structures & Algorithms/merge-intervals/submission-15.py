# DP/Greedy Type: Sort & Linear Merge (One-Pass)
# General Greedy Definition: An algorithmic paradigm that builds up a solution piece 
# by piece, always making the choice that seems best at that exact moment (locally optimal), 
# without worrying about the future impact. It hopes that these local choices lead 
# to a globally optimal solution.

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Crucial Step: Sort intervals by their start times i[0]
        intervals.sort(key=lambda i: i[0])
        
        # Seed the results array with the first interval to compare against
        res = [intervals[0]]
        
        # intervals[1:] slices the list to start iterating from the second element (index 1),
        # safely skipping the first element since it was already added to res.
        for i in intervals[1:]:
            # Get the end time of the most recently merged interval in our results
            lastEnd = res[-1][1]
            
            # If the current interval's start time i[0] is less than or equal to lastEnd, 
            # an overlap exists. Merge them by expanding the end boundary.
            if i[0] <= lastEnd:
                res[-1][1] = max(lastEnd, i[1])
            else:
                # No overlap! Safely append the current interval as a clean new slot.
                res.append(i)
                
        return res

# Time Complexity: O(n log n) -> Driven entirely by the initial sorting step. 
# Space Complexity: O(n) -> Required to store and return the new result list.
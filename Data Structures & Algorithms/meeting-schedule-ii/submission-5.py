# DP/Greedy Type: Chronological Event Scanning (Two-Pointer Chronological Simulation)
# General Greedy Definition: An algorithmic paradigm that builds up a solution piece 
# by piece, always making the choice that seems best at that exact moment (locally optimal), 
# without worrying about the future impact. It hopes that these local choices lead 
# to a globally optimal solution.

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        # Separate and sort start and end times independently
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        
        res = 0        # Tracks the peak number of concurrent rooms needed
        count = 0      # Tracks currently active meetings at any single moment
        
        s = 0          # Pointer for the start array
        e = 0          # Pointer for the end array
        
        # Process all meetings by their start events
        while s < len(intervals):
            # If a new meeting starts before the oldest active meeting ends
            if start[s] < end[e]:
                count += 1    # Occupy a new room
                s += 1        # Move to the next starting meeting
            else:
                count -= 1    # A meeting finished, free up a room
                e += 1        # Move to the next ending meeting
            
            # Record the maximum number of rooms required simultaneously
            res = max(res, count)
            
        return res

# Time Complexity: O(n log n) -> Dominated by sorting the start and end lists.
# Space Complexity: O(n) -> To store the separated arrays of start and end times.
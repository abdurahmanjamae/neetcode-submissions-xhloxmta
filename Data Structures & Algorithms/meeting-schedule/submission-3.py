# DP/Greedy Type: Sort & Linear Neighbor Check (One-Pass)
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
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        # Crucial Step: Sort the custom objects by their start attributes
        intervals.sort(key=lambda i: i.start)

        # Iterate through all meetings starting from index 1
        for i in range(1, len(intervals)):
            prevMeeting = intervals[i - 1]
            currMeeting = intervals[i]

            # If the previous meeting ends after the current meeting starts, conflict!
            if prevMeeting.end > currMeeting.start:
                return False
                
        return True

# Time Complexity: O(n log n) -> Driven entirely by sorting the n meetings.
# Space Complexity: O(n) -> Internal memory required for Python's sorting algorithm.
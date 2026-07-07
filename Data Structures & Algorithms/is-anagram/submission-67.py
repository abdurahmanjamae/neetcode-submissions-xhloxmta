# DP/Greedy Type: Sorted Sequence Comparison (Canonical Form Match)
# General Greedy Definition: An algorithmic paradigm that builds up a solution piece 
# by piece, always making the choice that seems best at that exact moment (locally optimal), 
# without worrying about the future impact. It hopes that these local choices lead 
# to a globally optimal solution.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths match up differently, they cannot possibly be anagrams
        if len(s) != len(t):
            return False
            
        # Sorting both strings reorganizes their characters into alphabetical order.
        # If they are anagrams, their sorted sequences will look exactly identical.
        return sorted(s) == sorted(t)

# Time Complexity: O(n log n) -> Sorting both strings of length n dominates the execution runtime.
# Space Complexity: O(n) -> Python's sorting algorithm (Timsort) creates a new list of characters.
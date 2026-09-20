class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Anagrams must have the same length
        if len(s) != len(t):
            return False
        
        freq = {}

        # Count each character in s
        for char in s:
            if char in freq:        # If we've seen this character before
                freq[char] += 1     # Increase its count by 1
            else:                   # If this is the first time seeing it
                freq[char] = 1      # Start its count at 1
        
        # Match characters from t against the counts
        for char in t:
            if char not in freq:    # Character does not exist in s
                return False

            if freq[char] == 0:     # # No more of this character left to match
                return False
            
            freq[char] -= 1         # One matching character found, decrease its count
        
        # All characters matched correctly
        return True

# Time: O(n)
# Space: O(n)
# Mental cue: same length → count s → subtract t → missing/zero = false
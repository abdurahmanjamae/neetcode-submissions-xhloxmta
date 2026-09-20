class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Anagrams must have the same length
        if len(s) != len(t):
            return False
        
        freq = {}

        # Count each character in s
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        # Subtract characters found in t
        for char in t:
            # Character does not exist in s
            if char not in freq:
                return False

            # Too many of this character in t
            if freq[char] == 0:
                return False
            
            freq[char] -= 1
        
        # All characters matched
        return True

# Time: O(n)
# Space: O(n)
# Mental cue: same length → count s → subtract t → missing/zero = false
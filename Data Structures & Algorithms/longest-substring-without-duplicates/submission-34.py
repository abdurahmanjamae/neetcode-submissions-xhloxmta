class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()  # Track unique characters in the current window
        left, res = 0, 0 

        for right in range(len(s)):
            # If we hit a duplicate, shrink the window from the left until it's gone
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            # Add the new character and update the maximum length found
            seen.add(s[right])
            res = max(res, right - left + 1)
            
        return res
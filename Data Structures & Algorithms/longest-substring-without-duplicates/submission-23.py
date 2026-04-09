class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()          # Stores characters currently in the window
        left, res = 0, 0      # left = start of window, res = longest length found

        for right in range(len(s)):   # Move right pointer through the string
            while s[right] in seen:   # If duplicate found, shrink window
                seen.remove(s[left])  # Remove left character from set
                left += 1             # Move left pointer forward
            
            seen.add(s[right])        # Add current character to window
            res = max(res, right - left + 1)  # Update max length

        return res   # Return longest substring length without duplicates

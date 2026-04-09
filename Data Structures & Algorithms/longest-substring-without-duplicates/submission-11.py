class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()          # store characters in the current window
        left = 0              # left pointer
        res = 0               # max length found

        # right pointer moves through the string
        for right in range(len(s)):
            # If character already in window, shrink from the left
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Add current character to the window
            seen.add(s[right])

            # Update max window size
            res = max(res, right - left + 1)

        return res

        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}        # stores last seen index of each character
        left = 0          # left boundary of current window (start of substring)
        res = 0           # tracks max length of substring without repeating chars

        for i in range(len(s)):              # iterate through each char index
            if s[i] in seen:                 # if char was seen before
                # move left to one past its last occurrence (avoid shrinking window backwards)
                left = max(seen[s[i]] + 1, left)
                
            seen[s[i]] = i                   # update last seen index for current char
            res = max(res, i - left + 1)     # update longest substring length found so far
        return res                           # return max length after traversing all chars


        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        res = 0

        for i in range(len(s)):
            if s[i] in seen:
                left = max(seen[s[i]] + 1, left)
                
            seen[s[i]] = i
            res = max(res, i-left + 1)
        return res 


        
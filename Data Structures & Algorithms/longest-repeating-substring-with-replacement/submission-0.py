class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}          # stores frequency of chars in window
        res = 0             # longest valid substring length

        left = 0            # left pointer of sliding window
        maxf = 0            # highest frequency char in window

        for right in range(len(s)):
            # add current char to window
            count[s[right]] = 1 + count.get(s[right], 0)

            # update max frequency seen in window
            maxf = max(maxf, count[s[right]])

            # if replacements needed > k, shrink window
            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1

            # update longest valid window size
            res = max(res, right - left + 1)

        return res

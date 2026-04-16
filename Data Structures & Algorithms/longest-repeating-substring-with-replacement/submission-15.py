class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # count maps each character to its frequency in the current window
        count = {}
        # left: start of window, res: longest valid length, maxf: highest freq of any char seen
        left, res, maxf = 0, 0, 0

        # Expand the 'right' boundary of the window one character at a time
        for right in range(len(s)):
            # Update frequency for the new character entering the window
            count[s[right]] = 1 + count.get(s[right], 0)
            
            # Update maxf: the most frequent character helps us minimize replacements
            maxf = max(maxf, count[s[right]])

            # MATH CHECK: (Total window size) - (count of most frequent char)
            # If the result is > k, we have too many "wrong" characters to replace.
            while (right - left + 1) - maxf > k:
                # The window is invalid. Shrink it from the left.
                count[s[left]] -= 1
                left += 1
            
            # Update the result with the maximum size the window has reached so far
            res = max(res, right - left + 1)
            
        return res
        
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            if char not in pairs:          # Opening bracket
                stack.append(char)
            else:                          # Closing bracket
                if not stack:
                    return False

                if stack[-1] != pairs[char]:
                    return False

                stack.pop()

        return len(stack) == 0
        
        
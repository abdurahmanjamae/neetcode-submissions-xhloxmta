class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Stores opening brackets

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }  # Closing bracket -> matching opening bracket

        for char in s:  # Check each bracket

            if char not in pairs:  # Opening bracket
                stack.append(char)  # Push it onto the stack

            else:  # Closing bracket

                if not stack:  # No opening bracket to match
                    return False

                if stack[-1] != pairs[char]:  # Top bracket does not match
                    return False

                stack.pop()  # Matching pair found, remove opening bracket

        return not stack  # True only if no unmatched brackets remain
        
        
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for char in s:
            # If char is a KEY in pairs, it's a closing bracket
            if char in pairs:
                # 1. Check if stack has something to pop
                # 2. Check if the popped opener matches the required opener
                if stack and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                # If it's NOT in pairs, it's an opening bracket; push it
                stack.append(char)

        # If stack is empty, all pairs matched perfectly
        return not stack
        
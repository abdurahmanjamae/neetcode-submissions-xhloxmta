class Solution:
    def isValid(self, s: str) -> bool:
        # Use a stack to keep track of opening brackets
        stack = []

        # Map each closing bracket to its matching opening bracket
        pairs = {')': '(', '}': '{', ']': '['}

        # Loop through each character in the string
        for char in s:
            # If it's an opening bracket, push it onto the stack
            if char in "{([":
                stack.append(char)
            else:
                # If the stack is empty, or the top doesn't match the closing bracket, it's invalid
                if not stack or stack.pop() != pairs[char]:
                    return False

        # If the stack is empty, all brackets were matched correctly
        return not stack

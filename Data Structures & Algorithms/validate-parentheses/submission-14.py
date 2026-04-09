class Solution:
    def isValid(self, s: str) -> bool:
        # use stack to keep track of opening brackets
        stack = []
        # map closing and opening brackets
        pairs = {')': '(', '}': '{', ']': '['}
        # loop through each char in s
        for char in s:
            # if its an opening bracket, push it on to the stack
            if char in "{([":
                stack.append(char)
            # if the stack is empty or top doesn't match closing pairs
            # it's invalid
            else:
                if not stack or stack.pop() != pairs[char]:
                    return False
        # if the stack is empty, all brackets are matched correctly
        return not stack
        
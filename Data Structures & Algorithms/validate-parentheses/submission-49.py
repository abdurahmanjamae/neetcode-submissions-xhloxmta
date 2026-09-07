class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }  # Closing bracket -> matching opening bracket

        for char in s:
            if char not in pairs:
                stack.append(char)
            
            else:
                if not stack:
                    return False
                
                if stack[-1] != pairs[char]:
                    return False
                
                stack.pop()
        
        return not stack
        
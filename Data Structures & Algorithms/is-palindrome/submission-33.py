class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers at the start and end of the string
        left, right = 0, len(s) - 1

        while left < right:
            # Move the left pointer forward if the character isn't a letter or number
            while left < right and not s[left].isalnum():
                left += 1
        
            # Move the right pointer backward if the character isn't a letter or number
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare characters (standardize to lowercase to ignore case sensitivity)
            if s[left].lower() != s[right].lower():
                return False # If they don't match, it's not a palindrome
            
            # Move both pointers inward to check the next pair
            left += 1
            right -= 1

        # If the pointers meet without finding a mismatch, it's a palindrome
        return True
        
        
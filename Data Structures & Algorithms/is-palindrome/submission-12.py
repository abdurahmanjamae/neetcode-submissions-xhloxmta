class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointers starting from both ends
        left, right = 0, len(s) - 1

        # Move pointers toward the center
        while left < right:
            # Skip non-alphanumeric characters on the left
            while left < right and not s[left].isalnum():
                left += 1

            # Skip non-alphanumeric characters on the right
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False

            # Move inward after a successful match
            left += 1
            right -= 1

        # All characters matched
        return True
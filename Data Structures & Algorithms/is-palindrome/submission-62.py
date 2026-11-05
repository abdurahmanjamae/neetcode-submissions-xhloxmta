class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Mental Cue: Two Pointers → Skip Invalid → Compare → Move Inward

        # Start pointers at opposite ends of the string
        left, right = 0, len(s) - 1

        # Continue until the pointers meet or cross
        while left < right:

            # Skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1

            # Skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare lowercase characters to ignore case differences
            if s[left].lower() != s[right].lower():
                return False  # Mismatch means not a palindrome

            # Move both pointers inward to compare the next pair
            left += 1
            right -= 1

        # No mismatches found, so it's a palindrome
        return True


# Runtime: O(n)
# Each pointer moves through the string at most once.

# Space: O(1)
# Only two pointers are used; no extra data structures.
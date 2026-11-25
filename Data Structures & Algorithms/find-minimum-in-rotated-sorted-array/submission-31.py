class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # If mid is less than right, the minimum must be at mid or to its left
            if nums[mid] < nums[right]:
                right = mid
            # If mid is greater than right, the minimum must be in the right half
            else:
                left = mid + 1

        # When left == right, we've narrowed it down to the smallest element
        return nums[left]

# Mental Cue: Compare mid with right → Keep the half containing the minimum → Repeat until left == right.
# RT: O(log n) - Binary search eliminates half the search space each iteration.
# Space: O(1) - Only left, right, and mid pointers are used.
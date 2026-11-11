# Container With Most Water (Two Pointers)

# Mental Cue:
# Start wide → Calculate area → Update max → Move shorter wall.
# Move the shorter wall because it limits the height of the water.
# Moving the taller wall only reduces the width without increasing
# the limiting height.

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Start with two pointers at opposite ends (maximum width)
        left, right = 0, len(heights) - 1

        # Track the maximum area found
        res = 0

        # Keep checking until the pointers meet
        while left < right:
            # Area = shorter wall (height) * distance between walls (width)
            # Use min() because water can only reach the shorter wall
            area = min(heights[left], heights[right]) * (right - left)

            # Update the maximum area if the current area is larger
            res = max(res, area)

            # Move the shorter wall inward to look for a taller wall
            # that could produce a larger area despite the smaller width
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        # Return the largest area found
        return res


# Runtime: O(n)
# Each pointer moves inward at most n times.
# We scan the array once instead of checking every pair.

# Space: O(1)
# Only use two pointers and a few variables.
# No additional data structures are created.
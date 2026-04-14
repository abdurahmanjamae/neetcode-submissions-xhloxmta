class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Start two pointers: one at the beginning, one at the end
        left, right = 0, len(heights) - 1
        
        # This will store the maximum water area found so far
        res = 0

        # Continue until the two pointers meet
        while left < right:
            # Calculate current container area:
            # width = distance between pointers
            # height = shorter of the two bars (water is limited by shorter wall)
            area = min(heights[left], heights[right]) * (right - left)
            
            # Update max area if current area is bigger
            res = max(res, area)

            # Move the pointer at the shorter height inward
            # Reason: moving the taller one cannot increase height,
            # but moving the shorter one might find a taller wall
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        # Return the largest area found
        return res

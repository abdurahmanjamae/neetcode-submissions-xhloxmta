class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right: 
            mid = (left + right) // 2

            # If mid > right, the rotation point (min) is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise, the min is at mid or in the left half
            else:
                right = mid
        
        # Binary search converges where left == right (the minimum)
        return nums[left]
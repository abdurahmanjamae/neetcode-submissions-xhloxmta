class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Found the target, return its index
            if nums[mid] == target:
                return mid
            
            # Check if the left half is sorted
            if nums[left] <= nums[mid]:
                # If target is within the sorted left range, move right pointer
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            # Otherwise, the right half must be sorted
            else:
                # If target is within the sorted right range, move left pointer
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        # Target not found in the array
        return -1
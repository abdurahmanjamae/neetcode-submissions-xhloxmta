class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # left pointer to mark the pos of next unique elements
        left = 1
        # right pointer to scan through the idx starting at 1
        for right in range (1, len(nums)):
            # if current value is not as prev value
            # that mean we found the unique value
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
        return left
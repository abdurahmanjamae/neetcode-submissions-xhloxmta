class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # left pointer 1 marks the pos of next unique element
        left = 1
        # right point to scan at idx 1
        for right in range(1, len(nums)):
            # if current element not equal to the prev element
            # it means we found a unique value
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
        return left
        
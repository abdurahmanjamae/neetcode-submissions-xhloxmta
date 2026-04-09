class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # left pointer marks where to place next valid element
        left = 0 
        # scan each elemnt with right pointer
        for right in range(len(nums)):
            # only keep numbers that are not equal to val
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left
        
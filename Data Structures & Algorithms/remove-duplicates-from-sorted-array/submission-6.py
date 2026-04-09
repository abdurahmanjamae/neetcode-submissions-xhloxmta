class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # left pointer to make the pos on next valid element
        left = 1
        # right pointer to scan start at idx 1
        for right in range(1, len(nums)):
            # if the current element is not equal to the prev, means we found a valid 1
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
        return left
        
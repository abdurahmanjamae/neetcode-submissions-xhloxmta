class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # left pointer 1 marks the pos to place the next unique element
        left = 1

        # right pointer (r) scans through the array starting from index 1 
        for right in range(1, len(nums)):
            # if current element is different from prev one
            # it means we found a new unique value
            if nums[right] != nums [right - 1]:
                nums[left] = nums[right]
                left += 1
        return left

nums = [0,0,1,1]
solution = Solution()
k = solution.removeDuplicates(nums)
print(k)
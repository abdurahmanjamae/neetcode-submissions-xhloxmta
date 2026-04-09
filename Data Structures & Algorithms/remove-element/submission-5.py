class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # left pointer to mark where to place the valid elements
        left = 0 
        # right pointer to scan 
        for right in range (len(nums)):
            # only keep # that are not equal to val
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left

# nums = [1,1,2,3,4], val = 1 --> [2,3,4] k = 3
# solution = Solution()
# k = solution.removeElement(nums,val)
# print(k)
# print(nums[:k])

# Run time is 0(n) since we scan through the for loop once
# Space complexity is O(1), we have a 1 left pointer and 1 right pointer



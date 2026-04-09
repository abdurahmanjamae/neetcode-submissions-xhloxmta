class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if diff in seen:
                return[seen[diff], i]
            seen[num] = i 
        
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, anchor in enumerate(nums):
            if anchor > 0:
                break
            if i > 0 and anchor == nums[i-1]:
                continue
            
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = anchor + nums[left] + nums[right]

                if current_sum > 0:
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    res.append([anchor, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return res
        
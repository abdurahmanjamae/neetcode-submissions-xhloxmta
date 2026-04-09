class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n # res[i] will hold the final product except nums[i]

        # Build prefix products (left side)
        left_product = 1
        for i in range(len(nums)):
            res[i] = left_product
            left_product *= nums[i]
        
        # Build suffix products (right side) and multiply into res
        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right_product  # multiply by everything to the right of i
            right_product *= nums[i] # update right_product to include nums[i]
        return res
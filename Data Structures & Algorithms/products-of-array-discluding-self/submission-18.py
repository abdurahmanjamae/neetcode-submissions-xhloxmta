class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n  # start with all 1s, result will be filled in

        # pass 1: store product of everything to the left of i
        left_product = 1
        for i in range(n):
            res[i] *= left_product
            left_product *= nums[i]
        
        # pass 2: multiply by product of everything to the right of i
        right_product = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right_product  # multiply by everything to the right of i
            right_product *= nums[i] # update right_product to include nums[i]
        return res






        
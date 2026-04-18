class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize the result array with 1s
        res = [1] * len(nums)

        # Pass 1: Calculate the prefix products (everything to the left)
        left_prod = 1
        for i in range(len(nums)):
            res[i] *= left_prod      # Current index gets the product of all previous numbers
            left_prod *= nums[i]     # Update left_prod to include the current number for the next index

        # Pass 2: Calculate the suffix products (everything to the right)
        right_prod = 1
        for i in range(len(nums) - 1, -1, -1): 
            res[i] *= right_prod     # Multiply current value by the product of all numbers to its right
            right_prod *= nums[i]    # Update right_prod to include current number for the next loop
            
        return res
        
        
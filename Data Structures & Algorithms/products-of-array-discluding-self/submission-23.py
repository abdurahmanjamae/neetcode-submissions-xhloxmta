class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Number of elements in the input array
        n = len(nums)

        # Result array initialized with 1s
        # res[i] will eventually hold the product of all elements except nums[i]
        res = [1] * n

        # left_product keeps track of the product of elements to the LEFT of i
        left_product = 1
        for i in range(n):
            # Multiply current value by product of all elements before i
            res[i] *= left_product

            # Update left_product to include nums[i]
            left_product *= nums[i]

        # right_product keeps track of the product of elements to the RIGHT of i
        right_product = 1
        for i in range(n - 1, -1, -1):
            # Multiply current value by product of all elements after i
            res[i] *= right_product

            # Update right_product to include nums[i]
            right_product *= nums[i]

        # res now contains product of array except self for each index
        return res

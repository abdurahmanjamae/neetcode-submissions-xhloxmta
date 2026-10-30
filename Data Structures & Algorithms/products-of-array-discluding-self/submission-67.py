class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize result array with 1s (multiplication identity)
        res = [1] * len(nums)

        # STEP 1: LEFT PASS (Prefix Products)
        # left_prod stores the product of all numbers BEFORE index i
        left_prod = 1

        for i in range(len(nums)):
            # Store the product of everything to the left of i
            res[i] *= left_prod

            # Include current number for the NEXT iteration
            left_prod *= nums[i]

        # STEP 2: RIGHT PASS (Suffix Products)
        # right_prod stores the product of all numbers AFTER index i
        right_prod = 1

        for i in range(len(nums) - 1, -1, -1):
            # Multiply existing left product by the right product
            # This gives the product of all numbers EXCEPT nums[i]
            res[i] *= right_prod

            # Include current number for the NEXT iteration
            right_prod *= nums[i]

        # Return the final products
        return res


# Mental Cue: Left → Right → Multiply
# 1. Left: Calculate the product of everything BEFORE each index.
# 2. Right: Calculate the product of everything AFTER each index.
# 3. Multiply: Combine left and right products to get the answer.
# No division needed.

# Runtime: O(n)
# - Left pass visits every element once: O(n)
# - Right pass visits every element once: O(n)
# - Total: O(n) + O(n) = O(n)

# Space: O(1) auxiliary space
# - Only use left_prod and right_prod variables.
# - res takes O(n) space but is the required output array.
# - Including the output array, total space is O(n).
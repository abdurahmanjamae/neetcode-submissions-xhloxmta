class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Mental Cue: Left → Right → Multiply
        # 1. Left: Product of everything before each index
        # 2. Right: Product of everything after each index
        # 3. Multiply: Combine both products (excluding current number)

        # Start with 1s because multiplying by 1 doesn't change the product
        res = [1] * len(nums)

        # STEP 1: LEFT PASS (Prefix Products)

        # Start at 1 because the first element has nothing to its left
        left_prod = 1

        # Loop left to right because we need everything before each element
        for i in range(len(nums)):
            # Store the product of all elements before index i
            res[i] *= left_prod

            # Include nums[i] for the next index
            left_prod *= nums[i]

        # STEP 2: RIGHT PASS (Suffix Products)

        # Start at 1 because the last element has nothing to its right
        right_prod = 1

        # Loop backward because we need the product of everything to the right of each element
        # Start at last index, stop before -1, move backward by 1
        for i in range(len(nums) - 1, -1, -1):
            # Multiply the stored left product by the right product
            res[i] *= right_prod

            # Include nums[i] for the next index moving left
            right_prod *= nums[i]

        # Return the product of all elements except themselves
        return res


# Runtime: O(n)
# - Left pass: O(n)
# - Right pass: O(n)
# - Total: O(n)

# Space: O(1) auxiliary space
# - Only use left_prod and right_prod variables
# - Output array res takes O(n) space (not counted as auxiliary space)
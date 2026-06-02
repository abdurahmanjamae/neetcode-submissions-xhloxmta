# DP Type: Bottom-Up Dynamic Programming (Tabulation)

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # res[i] stores the length of the LIS starting at index i
        res = [1] * len(nums)

        # Loop backwards through the array
        for i in range(len(nums) - 1, -1, -1):
            # Check all elements ahead of index i
            for j in range(i + 1, len(nums)):
                # If the next number is strictly greater, it can extend the subsequence
                if nums[i] < nums[j]:
                    res[i] = max(res[i], 1 + res[j])
                    
        # The answer is the maximum length found anywhere in our DP array
        return max(res)

# Time Complexity: O(n²)
# Two nested loops compare each element with all elements ahead of it.

# Space Complexity: O(n)
# Required for the 1D DP tracking array of size n.
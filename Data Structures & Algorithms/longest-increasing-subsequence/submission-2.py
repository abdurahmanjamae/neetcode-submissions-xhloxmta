# DP Type: Bottom-Up Dynamic Programming (Tabulation)

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # LIS[i] stores the length of the longest increasing subsequence starting at index i
        LIS = [1] * len(nums)

        # Loop backwards through the array
        for i in range(len(nums) - 1, -1, -1):
            # Check all elements ahead of index i
            for j in range(i + 1, len(nums)):
                # If the next number is strictly greater, it can extend the subsequence
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
                    
        # The answer is the maximum length found anywhere in our DP array
        return max(LIS)

# Time Complexity: O(n²)
# Two nested loops compare each element with all elements ahead of it.

# Space Complexity: O(n)
# Required for the 1D DP tracking array of size n.
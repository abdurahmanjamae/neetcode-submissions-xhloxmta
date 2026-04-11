class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort to use two-pointer logic and easily skip duplicates
        nums.sort()
        res = []

        for i, anchor in enumerate(nums):
            # Optimization: If anchor > 0, no possible triplet can sum to 0
            if anchor > 0:
                break
            
            # Skip duplicate anchors to avoid redundant triplets
            if i > 0 and anchor == nums[i-1]:
                continue

            # 4. TWO-POINTER SEARCH
            # Start 'left' at i + 1 to avoid using the 'anchor' twice 
            # and to skip combinations already checked.
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = anchor + nums[left] + nums[right]

                if current_sum > 0:
                    # Sum too large; decrease the right side
                    right -= 1
                elif current_sum < 0:
                    # Sum too small; increase the left side
                    left += 1
                else:
                    # Found a valid triplet
                    res.append([anchor, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicate values for the 'left' pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
        return res
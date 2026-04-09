class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array to enable the two-pointer technique
        # and make it easy to skip duplicates
        nums.sort()
        
        # Result list to store all unique triplets
        res = []

        # Iterate through each number, treating it as the "anchor"
        for i, anchor in enumerate(nums):

            # Optimization:
            # If the anchor is positive, no triplet can sum to 0
            # because the remaining numbers are also >= anchor
            if anchor > 0:
                break

            # Skip duplicate anchors to avoid duplicate triplets
            if i > 0 and anchor == nums[i - 1]:
                continue

            # Two pointers initialized to search remaining array
            left, right = i + 1, len(nums) - 1
            
            # Move pointers inward to find pairs that sum to -anchor
            while left < right:
                total = anchor + nums[left] + nums[right]

                # Sum is too large → decrease right pointer
                if total > 0:
                    right -= 1

                # Sum is too small → increase left pointer
                elif total < 0:
                    left += 1

                # Found a valid triplet
                else:
                    res.append([anchor, nums[left], nums[right]])

                    # Move both pointers to search for next valid pair
                    left += 1
                    right -= 1

                    # Skip duplicate values on the left to avoid repeats
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        # Return all unique triplets that sum to zero
        return res

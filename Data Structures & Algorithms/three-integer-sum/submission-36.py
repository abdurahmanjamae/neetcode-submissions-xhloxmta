class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        # PART 1: THE OUTER LOOP (The "Anchor")
        # Iterates through each number to treat it as the first element of a triplet.
        for i, anchor in enumerate(nums):
            if anchor > 0: break # Optimization: Positive anchors can't sum to 0
            
            # PART 2: OUTER SKIP (The "Anchor Duplicate" check)
            # Prevents starting a search with a value we've already fully explored.
            if i > 0 and anchor == nums[i-1]:
                continue

            # PART 3: THE INNER LOOP (Two-Pointer Search)
            # Uses 'i + 1' to only look forward and avoid reusing the anchor.
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = anchor + nums[left] + nums[right]

                if current_sum > 0:
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    res.append([anchor, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # PART 4: INNER SKIP (The "Pointer Duplicate" check)
                    # Once a match is found, skip identical values to find NEW triplets.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
        return res
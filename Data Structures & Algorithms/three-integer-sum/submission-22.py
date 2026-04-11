class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # PART 1: PREP (Sort for pointers and early exit)
        nums.sort()
        res = []

        for i, anchor in enumerate(nums):
            # Optimization: 3 positive numbers cannot sum to 0
            if anchor > 0:
                break
            
            # PART 2: OUTER GUARD (Skip used anchors to avoid duplicate triplets)
            if i > 0 and anchor == nums[i-1]:
                continue
            
            # PART 3: SEARCH (Two-pointer scan for target b + c = -a)
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = anchor + nums[left] + nums[right]

                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([anchor, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # PART 4: INNER GUARD (Skip identical values to keep results unique)
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res
        
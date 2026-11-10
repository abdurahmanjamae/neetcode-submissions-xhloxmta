class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array from smallest to largest.
        # This allows us to use two pointers because:
        # Moving left forward increases the sum.
        # Moving right backward decreases the sum.
        # Sorting also places duplicates next to each other.
        nums.sort()

        # Store all unique triplets that add up to zero.
        res = []

        # PART 1: THE OUTER LOOP (The "Anchor")

        # enumerate() gives us BOTH the index (i) and value (anchor).
        # Example: nums = [-4, -1, -1, 0, 1, 2]
        # First iteration: i = 0, anchor = -4
        # Second iteration: i = 1, anchor = -1
        for i, anchor in enumerate(nums):

            # Since the array is sorted, # Therefore, we cannot make a sum of zero.
            if anchor > 0:
                break

            # PART 2: SKIP DUPLICATE ANCHORS

            # i > 0 ensures we aren't on the first element.
            # nums[i - 1] is the previous number in the sorted list.
            # If the current anchor equals the previous anchor,
            # skip it because we already searched using that value.
            #
            # Example: [-4, -1, -1, 0, 1, 2]
            #              ^   ^
            # We only need to search using -1 as the anchor once.
            if i > 0 and anchor == nums[i - 1]:
                continue

            # PART 3: THE INNER LOOP (Two-Pointer Search)

            # Fix the anchor and search for TWO other numbers
            # that will make the total sum equal to zero.
            #
            # left starts AFTER the anchor (i + 1).
            # right starts at the LAST index in the array.
            #
            # Example: [-4, -1, -1, 0, 1, 2]
            #           ^    ^             ^
            #         anchor left         right
            left, right = i + 1, len(nums) - 1

            # Keep searching while the pointers haven't crossed.
            # Each iteration checks a different pair of numbers.
            while left < right:

                # Add the anchor and the two pointer values.
                # Our goal is to find three numbers that sum to 0.
                current_sum = anchor + nums[left] + nums[right]

                if current_sum < 0:
                    # Sum is too small (negative).
                    # Move left forward to get a LARGER number.
                    # This increases the sum because nums is sorted.
                    left += 1

                elif current_sum > 0:
                    # Sum is too large (positive).
                    # Move right backward to get a SMALLER number.
                    # This decreases the sum because nums is sorted.
                    right -= 1

                else:
                    # Sum equals ZERO!
                    # We found three numbers that form a valid triplet.
                    #
                    # Example: -1 + -1 + 2 = 0
                    # Save [-1, -1, 2] in our results.
                    res.append([anchor, nums[left], nums[right]])

                    # Move BOTH pointers inward.
                    # We already found this pair, so we need
                    # to search for a different combination.
                    left += 1
                    right -= 1

                    # PART 4: SKIP DUPLICATE POINTER VALUES

                    # After finding a valid triplet, check whether
                    # the new left value equals the previous left value.
                    #
                    # If they're identical, skip the duplicate.
                    # Otherwise, we could add the same triplet again.
                    #
                    # nums[left - 1] is the value we just moved past.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        # Return all unique triplets that add up to zero.
        return res


# MENTAL CUE:
# "Sort → Anchor → Skip Duplicates → Two Pointers → Adjust → Record"
#
# 1. SORT: Put numbers in order so pointer movements are predictable.
# 2. ANCHOR: Fix one number and search for two more.
# 3. SKIP: Ignore duplicate anchors to avoid repeated triplets.
# 4. TWO POINTERS: Left starts after anchor, right starts at end.
# 5. ADJUST:
#    - Sum < 0 → Move left forward to increase the sum.
#    - Sum > 0 → Move right backward to decrease the sum.
#    - Sum = 0 → Save the triplet and move both pointers.
# 6. RECORD: Skip duplicates to ensure unique triplets.
#
# TIME COMPLEXITY: O(n^2)
# - Sorting takes O(n log n).
# - Outer loop runs up to n times.
# - Two-pointer search takes O(n) per anchor.
# - Overall: O(n^2).
#
# SPACE COMPLEXITY: O(1) auxiliary space (excluding sorting/output)
# - Anchor and two pointers use constant extra space.
# - Python's sort can require O(n) additional space.
# - The output may contain O(n^2) triplets.
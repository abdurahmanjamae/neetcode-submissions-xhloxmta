
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Mental Cue: Set → Find Start → Count Forward → Update Longest

        # 1. Set: Convert list to a set for O(1) lookups
        num_set = set(nums)
        longest_seq = 0

        # 2. Find Start: Loop through unique numbers
        for num in num_set:
            # A sequence starts only if the previous number doesn't exist
            # Example: 1 is a start if 0 is not in the set
            if (num - 1) not in num_set:
                seq_len = 1

                # 3. Count Forward: Check if the next consecutive number exists
                # Example: 1 → 2 → 3 → 4
                while (num + seq_len) in num_set:
                    seq_len += 1

                # 4. Update Longest: Keep the maximum sequence length
                longest_seq = max(longest_seq, seq_len)

        return longest_seq


# Runtime: O(n)
# Each number is processed at most a constant number of times.
# We only count forward from the START of each sequence.

# Space: O(n)
# We use a set to store up to n unique numbers.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert list to a set for O(1) lookups
        num_set = set(nums)
        longest_seq = 0

        for num in num_set:
            # Check if 'num' is the START of a sequence
            # If (num - 1) exists, 'num' is just part of a sequence we'll catch later
            if (num - 1) not in num_set:
                seq_len = 1

                # Keep counting the consecutive numbers following this start
                while (num + seq_len) in num_set:
                    seq_len += 1

                # Update the global maximum length found so far
                longest_seq = max(longest_seq, seq_len)
        
        return longest_seq
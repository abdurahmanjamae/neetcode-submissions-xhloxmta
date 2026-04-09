class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_seq = 0

        for num in num_set:
            if (num - 1) not in num_set:
                seq_len = 1
                while (num + seq_len) in num_set:
                    seq_len += 1
                longest_seq = max(longest_seq, seq_len)
        return longest_seq
        
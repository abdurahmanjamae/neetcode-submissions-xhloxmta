class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count how many times each number appears
        count = Counter(nums)

        # Create buckets where index = frequency
        # freq[i] will store numbers that appear i times
        freq = [[] for _ in range(len(nums) + 1)]

        # Place each number into its frequency bucket
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []

        # Iterate from highest frequency to lowest
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)   # add most frequent numbers first
                if len(res) == k:
                    return res    # stop once we have k elements

 


        
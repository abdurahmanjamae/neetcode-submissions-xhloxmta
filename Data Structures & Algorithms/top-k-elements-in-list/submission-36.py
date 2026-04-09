class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count how many times each number appears
        # Result: {number: frequency}
        count = Counter(nums)

        # 2. Create "buckets" where the index represents the frequency
        # We use len(nums) + 1 because a number could appear up to 'n' times
        freq = [[] for i in range(len(nums) + 1)]
        
        # 3. Put numbers into the bucket corresponding to their count
        # Example: if '5' appears 3 times, it goes into freq[3]
        for num, cnt in count.items():
            freq[cnt].append(num)

        # 4. Iterate through buckets backwards (from highest frequency to lowest)
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                # 5. Stop once we've collected exactly 'k' elements
                if len(res) == k: 
                    return res
        
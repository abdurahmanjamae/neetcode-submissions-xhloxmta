class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []                 # create an empty list for the result
        for i in range(2):       # repeat the process twice
            for num in nums:       # go through each element in nums
                ans.append(num)    # add each element to ans
        return ans               # now ans = nums + nums



# Time Complexity: O(n) (each element appended twice → 2n ≈ n)
# Space Complexity: O(n) (new array of size 2n)
# nums = [1, 2, 3]
# solution = Solution()
# print(solution.getConcatenation(nums))  # [1,2,3,1,2,3]
        
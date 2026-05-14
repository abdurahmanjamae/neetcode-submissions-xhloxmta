class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return None
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return None
                curr.append(nums[j])
                dfs(j, curr, total+nums[j])
                curr.pop()
        dfs(0,[], 0)
        return res
        
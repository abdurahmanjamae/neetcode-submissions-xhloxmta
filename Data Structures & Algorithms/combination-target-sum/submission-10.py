class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        # Sorting helps in pruning the search tree early (optimization)
        nums.sort()

        def dfs(i, curr, total):
            # Base Case: We found a valid combination
            if total == target:
                # IMPORTANT: We must append a COPY of curr. 
                # If we append 'curr' directly, we are appending a reference.
                # Since 'curr' is modified later via .pop(), the results in 'res' 
                # would also change (and eventually end up empty).
                res.append(curr.copy())
                return None
            
            # Recursive Step: Try adding numbers starting from the current index 'i'
            # (Starting from 'i' allows us to reuse the same number multiple times)
            for j in range(i, len(nums)):
                # Optimization: If adding the current number exceeds target, 
                # because the list is sorted, all numbers after this will also exceed it.
                if total + nums[j] > target:
                    return None
                
                # 1. Action: Choose the number
                curr.append(nums[j])
                
                # 2. Recurse: Move deeper into the tree
                dfs(j, curr, total + nums[j])
                
                # 3. Backtrack: Remove the number to try other branches
                curr.pop()

        # Start DFS from index 0, with an empty path and a total sum of 0
        dfs(0, [], 0)
        return res

# --- COMPLEXITY ANALYSIS ---
# Let N be the number of candidates and T be the target value.
# Let M be the smallest value in candidates.
#
# Time Complexity: O(N^((T/M) + 1))
# The execution can be visualized as an N-ary tree where the max depth is T/M.
# In the worst case, we explore every branch.
#
# Space Complexity: O(T/M)
# This is determined by the maximum depth of the recursion stack and the 
# 'curr' list, which can grow up to T/M elements in size.
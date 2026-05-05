# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # This list will store our final levels: [[level0], [level1], [level2]]
        res = []

        def dfs(node, depth):
            # Base Case: If we reach a null pointer, stop the recursion
            if not node:
                return None
            
            # If 'res' doesn't have a sub-list for the current depth yet, create one.
            # Example: if depth is 2 and len(res) is 2 (indexes 0 and 1 exist), 
            # we add a new list for index 2.
            if len(res) == depth:
                res.append([])
            
            # Add the current node's value to its corresponding depth list
            res[depth].append(node.val)
            
            # Recurse to the left and right children, incrementing depth
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        # Kick off the recursion starting at the root (depth 0)
        dfs(root, 0)
        
        return res

# --- COMPLEXITY ANALYSIS ---
# Time Complexity: O(N)
# We visit every node in the tree exactly once.
#
# Space Complexity: O(H) or O(N) 
# 1. Recursion Stack: In the worst case (a skewed tree), the stack goes O(N) deep. 
#    In a balanced tree, it is O(log N), where H is the height of the tree.
# 2. Output List: We store all N nodes in the 'res' list, which is O(N).
        
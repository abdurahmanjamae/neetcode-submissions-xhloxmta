# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            # Base case: we reached the end of a branch
            if not node:
                return True
            
            # Check if current node stays within its allowed range
            if not (left < node.val < right):
                return False
            
            # Update boundaries: Left child must be < current, Right child must be > current
            return valid(node.left, left, node.val) and \
                   valid(node.right, node.val, right)

        # float("-inf") and float("inf") represent the initial 'no-limit' boundaries 
        # so that the root node can be any value without failing the first check.
        return valid(root, float("-inf"), float("inf"))

# Time Complexity: O(N) - We visit every node exactly once.
# Space Complexity: O(H) - Max depth of the recursion stack, where H is the tree height.
        
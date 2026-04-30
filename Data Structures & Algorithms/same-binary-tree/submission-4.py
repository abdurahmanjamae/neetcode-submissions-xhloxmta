# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both nodes are null; reached the end of identical paths
        if not p and not q:
            return True
        
        # Both nodes exist and values match; check children
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        # One node is null or values differ; trees are not the same
        else:
            return False

# Time Complexity: O(n), where n is the number of nodes in the smaller tree, 
# as we visit each node once.
# Space Complexity: O(n), where h is the height of the tree, 
# representing the maximum depth of the recursion stack.
        
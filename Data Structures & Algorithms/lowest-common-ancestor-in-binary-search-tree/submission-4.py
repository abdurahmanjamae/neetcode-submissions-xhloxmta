# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Base case: if we hit a null node
        if not root or not p or not q:
            return None
            
        # Both values are smaller than root; LCA must be in the left subtree
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        
        # Both values are larger than root; LCA must be in the right subtree
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        
        # We found the "split" point (or root is p or q); this is the LCA
        else:
            return root

# Time Complexity: O(h), where h is the height of the tree. 
# We visit one node per level. In a balanced tree, this is O(log n).
# Space Complexity: O(h), due to the recursion stack depth. 
# (An iterative version would bring this down to O(1)).
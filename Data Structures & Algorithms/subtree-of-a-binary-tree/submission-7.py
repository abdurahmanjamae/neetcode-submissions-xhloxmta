# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # An empty subRoot is technically a subtree of any tree
        if not subRoot: return True
        # If the main tree is empty but subRoot isn't, no match possible
        if not root: return False
        
        # Check if the trees are identical starting from the current node
        if self.sameTree(root, subRoot):
            return True
        
        # Recurse: Search for subRoot in the left or right children of root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both reached None; paths are identical
        if not p and not q:
            return True
        # Both exist and values match; strictly check children for equality
        if p and q and p.val == q.val:
            return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
        
        # Structural mismatch or value difference
        return False

# Time Complexity: O(N * M) - In the worst case, we run sameTree (O(M)) for every node in root (O(N)).
# Space Complexity: O(m+n) - The maximum depth of the recursion stack, where H is the height of root.
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # An empty subRoot is technically always a subtree
        if not subRoot: 
            return True
        # If main tree is empty but subRoot isn't, it can't be a subtree
        if not root: 
            return False
        
        # 1. Check if the trees are identical starting from the current node
        if self.sameTree(root, subRoot):
            return True
        
        # 2. Otherwise, recursively search for subRoot in the left or right children
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Both nodes are null, so they are identical at this position
        if not root and not subRoot:
            return True
        
        # If both exist and values match, check their children recursively
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and 
                    self.sameTree(root.right, subRoot.right))
        
        # Values don't match or one tree ended early
        return False

# Time Complexity: O(N * M) - In the worst case, we run sameTree (O(M)) for every node in root (O(N)).
# Space Complexity: O(m+n) - The maximum depth of the recursion stack, where H is the height of root.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if node is empty, stop
        if not root:
            return None
        
        # Swap the left and right children of current node
        root.left, root.right = root.right, root.left

        # Recursively repeat for the subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Return the modified tree
        return root

# Time: O(n) - visit every node once
# Space: O(n) - stack depth equals tree height
        
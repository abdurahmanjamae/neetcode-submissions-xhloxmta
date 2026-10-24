# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            nonlocal diameter

            if not node:
                return 0  # Empty subtree has height 0

            left = dfs(node.left)    # Get left subtree height
            right = dfs(node.right)  # Get right subtree height

            diameter = max(diameter, left + right)  # Update longest path

            return 1 + max(left, right)  # Return subtree height

        dfs(root)
        return diameter
        
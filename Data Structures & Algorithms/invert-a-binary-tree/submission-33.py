# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None  # No node to invert

        root.left, root.right = root.right, root.left  # Swap children

        self.invertTree(root.left)   # Invert left subtree
        self.invertTree(root.right)  # Invert right subtree

        return root  # Return inverted tree

# Time: O(n)
# Space: O(h)
# Mental cue: base case → swap → DFS left → DFS right → return root
        
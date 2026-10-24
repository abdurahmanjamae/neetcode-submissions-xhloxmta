class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0  # Track longest path in edges

        def dfs(node):
            nonlocal diameter  # Allow updating outer variable

            if node is None:
                return 0  # Base case: empty subtree

            left = dfs(node.left)    # Get left subtree height
            right = dfs(node.right)  # Get right subtree height

            diameter = max(diameter, left + right)  # Update longest path

            return 1 + max(left, right)  # Return subtree height

        dfs(root)        # Start DFS at root
        return diameter  # Return longest path

# Time: O(n) — Visit each node once
# Space: O(h) — Recursion stack depends on tree height
# h = log n (balanced tree), n (skewed tree)
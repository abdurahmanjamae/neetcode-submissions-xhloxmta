class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0  # Store the longest path found (in edges)

        def dfs(node):
            nonlocal diameter  # Allow DFS to update the outer variable

            if node is None:
                return 0  # Empty subtree has height 0

            left = dfs(node.left)    # Get height of left subtree
            right = dfs(node.right)  # Get height of right subtree

            # Update longest path passing through this node
            diameter = max(diameter, left + right)

            # Return height of current subtree to parent
            return 1 + max(left, right)

        dfs(root)        # Start DFS from the root
        return diameter  # Return longest path in edges
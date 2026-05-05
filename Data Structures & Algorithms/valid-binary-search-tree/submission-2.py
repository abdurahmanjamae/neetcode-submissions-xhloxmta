# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Define a helper function to carry the 'boundary' constraints down the tree
        def valid(node, left, right):
            # Base case: If we reach a null leaf, the path so far is valid
            if not node:
                return True
            
            # The current node's value MUST be strictly between the left and right boundaries
            # In the first call, these are -infinity and +infinity
            if not (left < node.val < right):
                return False
            
            # Recursively check subtrees:
            # For node.left: The maximum allowed value (right) becomes the current node's value
            # For node.right: The minimum allowed value (left) becomes the current node's value
            return valid(node.left, left, node.val) and \
                   valid(node.right, node.val, right)

        # Start the recursion with the root and the widest possible range
        return valid(root, float("-inf"), float("inf"))

# Time Complexity: O(N), where N is the number of nodes in the tree. 
# We visit every node exactly once to verify its value against the boundaries.

# Space Complexity: O(H), where H is the height of the tree. 
# This represents the maximum depth of the recursive call stack. 
# In the worst case (a skewed tree), it could be O(N); in a balanced tree, it is O(log N).
        
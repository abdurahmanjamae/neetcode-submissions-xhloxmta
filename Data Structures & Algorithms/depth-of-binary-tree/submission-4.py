# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Initialize stack with root and starting depth of 1
        stack = [[root, 1]]
        res = 0

        while stack:
            # Pop one pair and split it into node and depth variables
            node, depth = stack.pop()

            if node:
                # Track the maximum depth seen so far
                res = max(res, depth)
                # Push children to stack with incremented depth
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
            
        return res

# Time: O(n) - visit every node once
# Space: O(n) - stack stores at most the height of the tree
        
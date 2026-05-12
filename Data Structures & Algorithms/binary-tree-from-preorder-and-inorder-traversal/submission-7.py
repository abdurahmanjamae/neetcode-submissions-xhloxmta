# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base case: if lists are empty, we've reached a leaf's child (null)
        if not preorder or not inorder:
            return None
        
        # Preorder's first element is always the root of the current (sub)tree
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # Find where the root sits in the inorder list to split left/right subtrees
        mid = inorder.index(root_val)
        
        # Recursively build the left subtree
        # Inorder: everything before 'mid'
        # Preorder: the next 'mid' elements after the root
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        
        # Recursively build the right subtree
        # Inorder: everything after 'mid'
        # Preorder: everything remaining in the list
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root

# --- Complexity Analysis ---
# Time Complexity: O(n^2) 
# Reason: For every node (n), we perform an .index() search and list slicing, 
# both of which can take O(n) time in the worst case. 
# (Note: This can be optimized to O(n) using a hash map for lookups).
#
# Space Complexity: O(n)
# Reason: In the worst case (a skewed tree), the recursion stack will be n deep. 
# Additionally, the list slicing creates new copies of the arrays at each step.
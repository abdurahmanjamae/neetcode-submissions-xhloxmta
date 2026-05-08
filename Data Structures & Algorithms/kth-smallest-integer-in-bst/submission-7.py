# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Array to store node values in sorted order
        arr = []

        def dfs(node):
            # Base case: if we reach a null leaf, stop recursion
            if not node:
                return None
            
            # Binary Search Trees (BST) have a special property: 
            # An In-Order Traversal (Left -> Root -> Right) visits nodes 
            # in ascending (sorted) order.
            
            # 1. Visit the left subtree (smaller values)
            dfs(node.left)
            
            # 2. Visit the current node and add to our list
            arr.append(node.val)
            
            # 3. Visit the right subtree (larger values)
            dfs(node.right)
            
        # Start the traversal from the root
        dfs(root)
        
        # Since the array is now sorted, the kth smallest element 
        # is at index k-1 (due to 0-based indexing)
        return arr[k-1]

# Time Complexity: O(N) where N is the number of nodes in the tree. 
# We visit every node exactly once to build the sorted list.

# Space Complexity: O(N) for the 'arr' list to store all node values, 
# plus O(H) for the recursion stack where H is the height of the tree.
        
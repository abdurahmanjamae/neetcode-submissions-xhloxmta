"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Hash map to track original nodes and their corresponding cloned copies
        old_to_new = {}

        def dfs(node):
            # Base case: handle empty graph input
            if not node:
                # Note: This check only hits on the initial call if the input is None.
                # In recursion, we only pass existing neighbors, so it won't hit here again.
                return None
                
            # If the node was already cloned, return the existing copy to avoid cycles
            if node in old_to_new:
                return old_to_new[node]
            
            # Create a deep copy of the current node (without neighbors yet)
            copy = Node(node.val)
            old_to_new[node] = copy

            # Recursively clone all neighbors and add them to the copy's list
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
                
            return copy
            
        return dfs(node)

# Time Complexity: O(V + E) 
# We visit every vertex (V) exactly once and traverse along every edge (E) to check neighbors.

# Space Complexity: O(V)
# The old_to_new hash map stores a reference to all V nodes. 
# Additionally, the recursive call stack takes O(H) space where H is the height of the graph, 
# which in the worst-case (a straight line graph) can be O(V).
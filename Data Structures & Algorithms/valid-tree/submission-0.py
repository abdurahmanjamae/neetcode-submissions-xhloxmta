from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Step 1: An empty graph or single node with no edges is technically a valid tree
        if not n:
            return True
            
        # Map out our nodes into an adjacency list
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)  # Undirected graph, so add both directions
            
        visited = set()

        def dfs(node, prev):
            # Base Case 1: If we hit a node already in our visited set, a cycle exists!
            if node in visited:
                return False
                
            visited.add(node)
            
            # Recursively check all neighbors
            for nei in graph[node]:
                # Crucial step: skip bouncing back to the node we literally just came from
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
                    
            return True

        # Step 2: Check for a cycle starting from node 0
        if not dfs(0, -1):
            return False
            
        # Step 3: Check connectivity. The tree is only valid if we reached every single node.
        return len(visited) == n

# Time Complexity: O(V + E)
# We traverse every node and edge exactly once during the DFS traversal.

# Space Complexity: O(V + E)
# To store the adjacency map, the visited set, and the recursive call stack.
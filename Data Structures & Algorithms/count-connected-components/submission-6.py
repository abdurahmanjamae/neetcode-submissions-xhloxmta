class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Map out our nodes into an adjacency list
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)  # Undirected graph, so add both directions
            
        visited = set()
        components = 0

        def dfs(node):
            visited.add(node)
            # Recursively visit all unvisited neighbors to clear out this entire component
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        # Loop through every possible node in the graph
        for i in range(n):
            if i not in visited:
                # We found a node that hasn't been touched yet -> it's a new component!
                components += 1
                dfs(i)  # Flood-fill through the component to mark all its nodes as visited
                
        return components

# Time Complexity: O(V + E)
# We look at each node (V) and traverse each undirected edge (E) to build and search the graph.

# Space Complexity: O(V + E)
# For the adjacency list graph representation, the visited set, and the recursive call stack
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map out our courses into an adjacency list (e.g., course -> list of its prerequisites)
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
            
        # Set to track courses currently in our active DFS recursion stack
        visiting = set()

        def dfs(node):
            # Base Case 1: Found a cycle! (Looping back to a node in the active stack)
            if node in visiting:
                return False
            # Base Case 2: This node has already been fully processed and verified safe
            if graph[node] == []:
                return True
                
            # Mark this node as actively being explored
            visiting.add(node)
            
            # Recursively check all prerequisites for this node
            for pre in graph[node]:
                if not dfs(pre):
                    return False
                    
            # Backtrack: Remove from the active stack and mark as fully cleared
            visiting.remove(node)
            graph[node] = [] # Optimization: clearing prerequisites means we don't re-check it later
            
            return True

        # Run DFS for every single course to handle disconnected parts of the graph
        for i in range(numCourses):
            if not dfs(i):
                return False
                
        return True

# Time Complexity: O(V + E)
# We visit each course node (V) and traverse each prerequisite edge (E) exactly once.

# Space Complexity: O(V + E)
# The graph dictionary uses O(V + E) space. The visiting set and recursive call stack 
# each use up to O(V) space.
        
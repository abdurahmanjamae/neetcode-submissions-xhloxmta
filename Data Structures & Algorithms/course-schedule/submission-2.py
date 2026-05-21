from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map out our courses into an adjacency list (e.g., course -> list of its prerequisites)
        pre_map = defaultdict(list)
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
            
        # Set to track courses currently in our active DFS recursion stack
        visiting = set()

        def dfs(crs):
            # Base Case 1: Found a cycle! (Looping back to a course in the active stack)
            if crs in visiting:
                return False
            # Base Case 2: This course has already been fully processed and verified safe
            if pre_map[crs] == []:
                return True
                
            # Mark this course as actively being explored
            visiting.add(crs)
            
            # Recursively check all prerequisites for this course
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
                    
            # Backtrack: Remove from the active stack and mark as fully cleared
            visiting.remove(crs)
            pre_map[crs] = [] # Optimization: clearing prerequisites means we don't re-check it later
            
            return True

        # Run DFS for every single course to handle disconnected parts of the graph
        for crs in range(numCourses):
            if not dfs(crs):
                return False
                
        return True
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Map out our courses into an adjacency list
        # Map: course -> list of its prerequisites
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
            
        # Set to track courses currently in our active DFS recursion stack
        visiting = set()

        def dfs(crs):
            # Base Case 1: Found a cycle! (We looped back to a course we are currently exploring)
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

        # Step 2: Run DFS for every single course to handle disconnected graphs
        for crs in range(numCourses):
            if not dfs(crs):
                return False
                
        return True
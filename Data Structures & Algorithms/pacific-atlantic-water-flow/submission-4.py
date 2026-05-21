class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return 

        rows, cols = len(heights), len(heights[0])
        p_reachable = set()
        a_reachable = set()

        def dfs(r, c, reachable_set, prev_heights):
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                (r,c) in reachable_set or heights[r][c] < prev_heights):
                return 
            
            reachable_set.add((r,c))

            dfs(r+1, c, reachable_set, heights[r][c])
            dfs(r-1, c, reachable_set, heights[r][c])
            dfs(r, c+1, reachable_set, heights[r][c])
            dfs(r, c-1, reachable_set, heights[r][c])

        for r in range(rows):
            dfs(r, 0, p_reachable, heights[r][0])
            dfs(r, cols-1, a_reachable, heights[r][cols-1])
        
        for c in range(cols):
            dfs(0, c, p_reachable, heights[0][c])
            dfs(rows-1, c, a_reachable, heights[rows-1][c])
        return list(p_reachable.intersection(a_reachable))
        
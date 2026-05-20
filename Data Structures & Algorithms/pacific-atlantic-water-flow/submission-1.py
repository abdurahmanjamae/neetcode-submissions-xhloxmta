class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #Edge case check: return empty list immediately if the input grid is empty or malformed
        if not heights or not heights[0]:
            return []
            
        ROWS, COLS = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r, c, reachable_set, prev_height):
            # If out of bounds, already visited, or the water can't flow "up" 
            # (current height is lower than where we just came from), stop.
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                (r, c) in reachable_set or heights[r][c] < prev_height):
                return
            
            # Mark this cell as reachable by the current ocean
            reachable_set.add((r, c))
            
            # Look in all 4 directions
            dfs(r + 1, c, reachable_set, heights[r][c])
            dfs(r - 1, c, reachable_set, heights[r][c])
            dfs(r, c + 1, reachable_set, heights[r][c])
            dfs(r, c - 1, reachable_set, heights[r][c])

        # 1. Start DFS from the horizontal borders (Top row = Pacific, Bottom row = Atlantic)
        for c in range(COLS):
            dfs(0, c, pacific_reachable, heights[0][c])
            dfs(ROWS - 1, c, atlantic_reachable, heights[ROWS - 1][c])

        # 2. Start DFS from the vertical borders (Left col = Pacific, Right col = Atlantic)
        for r in range(ROWS):
            dfs(r, 0, pacific_reachable, heights[r][0])
            dfs(r, COLS - 1, atlantic_reachable, heights[r][COLS - 1])

        # 3. Find the cells that exist in both sets
        return list(pacific_reachable.intersection(atlantic_reachable))
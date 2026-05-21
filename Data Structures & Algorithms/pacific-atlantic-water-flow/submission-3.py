class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Edge case check: return empty list immediately if the input grid is empty or malformed
        if not heights or not heights[0]:
            return []
            
        rows, cols = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r, c, reachable_set, prev_heights):
            # Clean guard clause: handles out-of-bounds, duplicates, and blocks flow if the next cell is lower
            if (r < 0 or r >= rows or c < 0 or c >= cols 
                or (r, c) in reachable_set or heights[r][c] < prev_heights):
                return
            
            # Mark this cell as reachable by the current ocean
            reachable_set.add((r, c))
            
            # Look in all 4 directions
            dfs(r + 1, c, reachable_set, heights[r][c])
            dfs(r - 1, c, reachable_set, heights[r][c])
            dfs(r, c + 1, reachable_set, heights[r][c])
            dfs(r, c - 1, reachable_set, heights[r][c])

        # 1. Start DFS from the vertical borders (Left col = Pacific, Right col = Atlantic)
        for r in range(rows):
            dfs(r, 0, pacific_reachable, heights[r][0])
            dfs(r, cols - 1, atlantic_reachable, heights[r][cols - 1])

        # 2. Start DFS from the horizontal borders (Top row = Pacific, Bottom row = Atlantic)
        for c in range(cols):
            dfs(0, c, pacific_reachable, heights[0][c])
            dfs(rows - 1, c, atlantic_reachable, heights[rows - 1][c])

        # 3. Find the cells that exist in both sets
        return list(pacific_reachable.intersection(atlantic_reachable))

# Time Complexity: O(M * N)
# Where M is the number of rows and N is the number of columns. Each cell in the grid is visited 
# a constant number of times (at most twice—once for each ocean traversal).

# Space Complexity: O(M * N)
# In the worst-case scenario, the reachable sets (`pacific_reachable` and `atlantic_reachable`) 
# will store all cells in the grid. Additionally, the internal recursion stack for DFS can 
# go up to O(M * N) deep if the flow path wraps across the entire grid.
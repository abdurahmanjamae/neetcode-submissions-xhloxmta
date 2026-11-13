class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Get grid dimensions and initialize island counter
        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        def dfs(i, j):
            # Base Case: Stop if out of bounds or cell is water ('0')
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != '1':
                return None
            else:
                # Mark current land cell as visited (sink it)
                grid[i][j] = '0'
                
                # Recursively explore all 4 adjacent directions
                dfs(i, j+1)  # Right
                dfs(i+1, j)  # Down
                dfs(i, j-1)  # Left
                dfs(i-1, j)  # Up

        # Scan every cell in the grid
        for i in range(rows):
            for j in range(cols):
                # When unvisited land is found, it's a new island
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)  # Run DFS so connected land is not counted again
        
        return num_islands  

# Time: O(m * n) — Each cell is visited at most once.
# Space: O(m * n) — DFS recursion stack in the worst case.
# m = number of rows, n = number of columns.

# Mental Cue: Scan → Find Land → Count → Sink → Explore 4 Directions
#
# 1. Scan: Loop through every cell.
# 2. Find Land: If cell is '1', you found a new island.
# 3. Count: Increment island counter.
# 4. Sink: Mark visited land as '0'.
# 5. Explore: DFS in all 4 directions (→ ↓ ← ↑).
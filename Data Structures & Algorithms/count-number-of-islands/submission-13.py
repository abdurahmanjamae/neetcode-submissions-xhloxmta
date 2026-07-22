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
                    dfs(i, j)  # Sink the entire connected island
        
        return num_islands  # Time: O(m * n), Space: O(m * n)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        num_island = 0 

        def dfs(i,j):
            # base case, boundaries
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != '1':
                return

            # mark current land cell as visited
            else:
                grid[i][j] = '0'

            # explore all 4 adj directions
            dfs(i, j+1) # right
            dfs(i+1, j) # down
            dfs(i, j-1) # left
            dfs(i-1, j) # up

        # scan every cell in grid
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    num_island +=1
                    dfs(i,j)
        
        return num_island

        
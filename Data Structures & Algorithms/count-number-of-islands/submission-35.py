class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            #base case of boundaries
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != '1':
                return None

            #sink
            else:
                grid[i][j] = '0'
            
                # explore all 4 directions
                dfs(i, j+1) # right
                dfs(i+1, j) # Downward
                dfs(i, j-1) # left
                dfs(i-1, j) # upward



        # scan every cell
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i,j)

        return count



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        num_island = 0 

        def dfs(i,j):
            stack = [(i, j)]

            while stack:
                i, j = stack.pop()
            # base case, boundaries
                if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != '1':
                    continue

                # mark current land cell as visited
                
                grid[i][j] = '0'

                # explore all 4 adj directions
                stack.append((i, j+1)) # right
                stack.append((i+1, j)) # down
                stack.append((i, j-1)) # left
                stack.append((i-1, j)) # up

        # scan every cell in grid
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    num_island +=1
                    dfs(i,j)
        
        return num_island

        
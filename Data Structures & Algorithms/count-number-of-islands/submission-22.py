class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        def dfs(i, j):
            stack = [(i, j)]

            # mark starting land cell as visited
            grid[i][j] = '0'

            while stack:
                row, col = stack.pop()

                # explore all 4 adjacent directions
                directions = [
                    (0, 1),   # right
                    (1, 0),   # down
                    (0, -1),  # left
                    (-1, 0)   # up
                ]

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    # boundary check and check for unvisited land
                    if (0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == '1' ):
                        # mark as visited before adding to stack
                        grid[new_row][new_col] = '0'
                        stack.append((new_row, new_col))

        # scan every cell in the grid
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)

        return num_islands
# DP/Greedy Type: Matrix In-Place State Storage (Single-Pass Flagging)
# General Greedy Definition: An algorithmic paradigm that builds up a solution piece 
# by piece, always making the choice that seems best at that exact moment (locally optimal), 
# without worrying about the future impact. It hopes that these local choices lead 
# to a globally optimal solution.

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Get grid dimensions and initialize flag for tracking the first row
        rows, cols = len(matrix), len(matrix[0])
        rowZero = False

        # Step 1: Sweep the entire matrix once to mark tracking flags in row 0 and col 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0  # Flag column j
                    if i > 0:
                        matrix[i][0] = 0  # Flag row i
                    else:
                        rowZero = True  # Flag row 0 separately since matrix[0][0] tracks col 0

        # Step 2: Zero out the inner grid cells based on the header flags
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        # Step 3: Zero out the first column if the top-left cell was flagged
        if matrix[0][0] == 0:
            for i in range(rows):
                matrix[i][0] = 0

        # Step 4: Zero out the first row if the rowZero flag is True
        if rowZero:
            for j in range(cols):
                matrix[0][j] = 0

# Time Complexity: O(m * n) -> Two highly compact passes over the grid.
# Space Complexity: O(1) -> Maximizes the matrix headers for zero auxiliary space.
# DP/Greedy Type: Matrix In-Place State Storage (In-Place Flagging)
# General Greedy Definition: An algorithmic paradigm that builds up a solution piece 
# by piece, always making the choice that seems best at that exact moment (locally optimal), 
# without worrying about the future impact. It hopes that these local choices lead 
# to a globally optimal solution.

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False
        colZero = False
        
        # Step 1: Determine if the first row or first column needs to be zeroed out
        for j in range(COLS):
            if matrix[0][j] == 0:
                rowZero = True
        for i in range(ROWS):
            if matrix[i][0] == 0:
                colZero = True
                
        # Step 2: Use the first row and col as markers for the rest of the matrix
        for i in range(1, ROWS):
            for j in range(1, COLS):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        # Step 3: Zero out internal cells based on the markers in the first row/col
        for i in range(1, ROWS):
            for j in range(1, COLS):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        # Step 4: Finally, zero out the first row and first column if flags were set
        if rowZero:
            for j in range(COLS):
                matrix[0][j] = 0
        if colZero:
            for i in range(ROWS):
                matrix[i][0] = 0

# Time Complexity: O(m * n) -> Two full passes over the matrix elements.
# Space Complexity: O(1) -> Storage utilizes existing cells, avoiding extra arrays.
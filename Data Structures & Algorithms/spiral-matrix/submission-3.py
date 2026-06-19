# DP/Greedy Type: Matrix Boundary Shrinking Simulation (Layer-by-Layer)
# General Greedy Definition: An algorithmic paradigm that builds up a solution piece 
# by piece, always making the choice that seems best at that exact moment (locally optimal), 
# without worrying about the future impact. It hopes that these local choices lead 
# to a globally optimal solution.

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        # Exclusive boundaries: right and bottom point one index past the valid elements
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # 1. Move right along the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            
            # 2. Move down along the right column (using right - 1 for valid index)
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            
            # Guard check to ensure boundaries haven't crossed mid-layer
            if not (left < right and top < bottom):
                break
                
            # 3. Move left along the bottom row (using bottom - 1 for valid index)
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            
            # 4. Move up along the left column
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res

# Time Complexity: O(m * n) -> We visit exactly every cell in the m x n matrix once.
# Space Complexity: O(n) -> Storing the results list (O(1) auxiliary space beyond the output).
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Time Complexity: O(1)
        Space Complexity: O(1)

        Why:
        - The board size is always fixed at 9x9. * that's why its constant
        - Otherwise, if we gneralize to an n x x = O(n^2)
        - We loop over rows, columns, and 3x3 boxes, but the total work
          is bounded by a constant (81 cells).
        - The sets used can hold at most 9 elements, which is also constant.
        """

        # -------------------------
        # Validate each row
        # -------------------------
        for i in range(9):
            seen = set()  # stores numbers already seen in this row
            for j in range(9):
                item = board[i][j]

                # If the number is already seen, row is invalid
                if item in seen:
                    return False
                # Ignore empty cells, only track numbers
                elif item != '.':
                    seen.add(item)

        # -------------------------
        # Validate each column
        # -------------------------
        for i in range(9):
            seen = set()  # stores numbers already seen in this column
            for j in range(9):
                item = board[j][i]

                # Duplicate found in column
                if item in seen:
                    return False
                # Add non-empty values
                elif item != '.':
                    seen.add(item)

        # -------------------------
        # Validate each 3x3 box
        # -------------------------
        for box_row in range(3):
            for box_col in range(3):
                seen = set()  # stores numbers seen in this 3x3 box

                # Top-left corner of the current 3x3 box
                start_row = box_row * 3
                start_col = box_col * 3

                # Traverse the 3x3 box
                for i in range(3):
                    for j in range(3):
                        item = board[start_row + i][start_col + j]

                        # Duplicate found in the box
                        if item in seen:
                            return False
                        # Track non-empty values
                        elif item != '.':
                            seen.add(item)

        # If all checks pass, the board is valid
        return True

                    
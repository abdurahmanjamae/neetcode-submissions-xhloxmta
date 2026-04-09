class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # validate rows 
        for i in range(9):
            seen = set()
            for j in range(9):
                item = board[i][j]
                if item in seen:
                    return False
                elif item != '.':
                    seen.add(item)

        # validiate col

        for i in range(9):
            seen = set()
            for j in range(9):
                item = board[j][i]
                if item in seen:
                    return False
                elif item != '.':
                    seen.add(item)

        # validate box
        for box_row in range(3):
            for box_col in range(3):
                seen = set()
                start_row = box_row * 3
                start_col = box_col * 3

                for i in range(3):
                    for j in range(3):
                        item = board[start_row + i][start_col + j]
                        if item in seen:
                            return False
                        elif item != '.':
                            seen.add(item)
        return True
        
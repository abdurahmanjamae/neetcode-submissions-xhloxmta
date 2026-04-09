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
                

        # validate col

        for i in range(9):
            seen = set()
            for j in range(9):
                item = board[j][i]
                if item in seen:
                    return False
                elif item != '.':
                    seen.add(item)
                
        #validate boxes

        for box_row in range(3):
            for box_col in range(3):
                seen = set()
                show_row = box_row * 3
                show_col = box_col * 3

                for i in range(3):
                    for j in range(3):
                        item = board[show_row + i] [show_col + j]
                        if item in seen:
                            return False
                        elif item != ".":
                            seen.add(item)
        return True


        
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        # Path set ensures we don't visit the same cell twice in a single word path
        path = set()

        def dfs(r, c, i):
            # BASE CASE: If index matches word length, we found the whole word
            if i == len(word):
                return True
            
            # GUARD CLAUSE: Return False if:
            # 1. Out of bounds (r, c)
            # 2. Character mismatch board[r][c] != word[i]
            # 3. Cell already in current path
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
                word[i] != board[r][c] or (r, c) in path):
                return False
            
            # RECURSIVE STEP:
            # 1. Add current cell to path before exploring neighbors
            path.add((r, c))
            
            # 2. Explore all 4 adjacent directions (Up, Down, Left, Right)
            # We use 'or' because we only need ONE of these paths to be True
            res = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or 
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )
            
            # 3. BACKTRACKING: Remove cell from path so other branches 
            # of the search can potentially use this cell
            path.remove((r, c))
            
            return res
    
        # BRUTE FORCE START: Check every single cell as a potential starting point
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
                    
        return False

# TIME AND SPACE COMPLEXITY:
# Time: O(N * M * 4^L) 
# -- Where N*M is the board size and L is the length of the word. 
# -- For every cell, we explore 4 directions recursively up to depth L.
# Space: O(L) 
# -- The recursion stack and the 'path' set will at most hold L elements.
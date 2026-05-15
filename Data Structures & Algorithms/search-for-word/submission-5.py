class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        # Track the current path to avoid using the same cell twice
        path = set()

        def dfs(r, c, i):
            # BASE CASE: Success! Found all characters in the word
            if i == len(word):
                return True
            
            # GUARD CLAUSE: Invalid move if out of bounds, wrong char, or already visited
            if (min(r, c) < 0 or r >= rows or c >= cols or word[i] != board[r][c] or (r, c) in path):
                return False
            
            # PRE-RECURSION: Add current cell to path (Mark as visited)
            path.add((r, c))
            
            # RECURSION: Try all 4 directions (Down, Up, Right, Left)
            res = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or 
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )
            
            # BACKTRACK: Remove cell from path to allow other search branches to use it
            path.remove((r, c))
            return res
    
        # OUTER LOOP: Start a DFS search from every cell in the grid
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False

# RT (Run Time) Complexity: O(N * M * 4^L)
# N * M is the board size; for each cell, we explore 4 directions up to the word length L.

# Space Complexity: O(L)
# The recursion stack and the 'path' set grow linearly with the length of the word L.
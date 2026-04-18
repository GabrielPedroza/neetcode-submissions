class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        ROWS, COLS = len(board), len(board[0])

        for row in range(ROWS):
            for col in range(COLS):
                curr_cell = board[row][col]

                if curr_cell == ".": continue

                curr_cell_key = f"{row // 3}-{col // 3}"
            
                if curr_cell in rows[row] or curr_cell in cols[col] or curr_cell in squares[curr_cell_key]:
                    return False
            
                rows[row].add(curr_cell)
                cols[col].add(curr_cell)
                squares[curr_cell_key].add(curr_cell)
        
        return True
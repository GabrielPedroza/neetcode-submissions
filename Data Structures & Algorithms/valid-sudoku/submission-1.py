class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                curr_square = board[r][c]
                if curr_square == '.': continue

                square_key = f"{r // 3}-{c // 3}"

                if curr_square in rows[r] or curr_square in cols[c] or curr_square in squares[square_key]:
                    return False
                
                rows[r].add(curr_square)
                cols[c].add(curr_square)
                squares[square_key].add(curr_square)
        
        return True
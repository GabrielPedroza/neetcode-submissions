class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # down, up, right, left
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or (r, c) in visited
                or board[r][c] != word[i]
            ):
                return
            
            if i == len(word) - 1:
                return True

            visited.add((r, c))

            for dr, dc in directions:
                if dfs(r + dr, c + dc, i + 1):
                    return True
            
            visited.remove((r, c))
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False

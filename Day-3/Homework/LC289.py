class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        Time Complexity: O(m * n)
        Space Complexity: O(1)
        """
        m, n = len(board), len(board[0])
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for r in range(m):
            for c in range(n):
                live_neighbors = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        live_neighbors += board[nr][nc] & 1

                # Rule 1-3: Live cell lives on with 2 or 3 neighbors
                if (board[r][c] & 1) == 1:
                    if live_neighbors in (2, 3):
                        board[r][c] |= 2
                # Rule 4: Dead cell becomes live with exactly 3 neighbors
                else:
                    if live_neighbors == 3:
                        board[r][c] |= 2

        # Shift right to apply next state
        for r in range(m):
            for c in range(n):
                board[r][c] >>= 1
                
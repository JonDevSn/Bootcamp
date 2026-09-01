class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        orig_color = image[sr][sc]
        if orig_color == color:
            return image

        rows, cols = len(image), len(image[0])

        def dfs(r: int, c: int):
            image[r][c] = color
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == orig_color:
                    dfs(nr, nc)

        dfs(sr, sc)
        return image
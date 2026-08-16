class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        """
        Time Complexity: O(m * n)
        Space Complexity: O(1) auxiliary (excluding output array)
        """
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        res = []
        r = c = 0
        direction = 1  # 1: up-right, -1: down-left

        for _ in range(m * n):
            res.append(mat[r][c])

            if direction == 1:
                if c == n - 1:
                    r += 1
                    direction = -1
                elif r == 0:
                    c += 1
                    direction = -1
                else:
                    r -= 1
                    c += 1
            else:
                if r == m - 1:
                    c += 1
                    direction = 1
                elif c == 0:
                    r += 1
                    direction = 1
                else:
                    r += 1
                    c -= 1

        return res
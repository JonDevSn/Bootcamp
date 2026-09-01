class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []

        def backtrack(start: int, path: list[int]):
            if len(path) == k:
                res.append(path[:])
                return

            # Pruning: ensure there are enough remaining elements to complete combination of size k
            needed = k - len(path)
            for i in range(start, n - needed + 2):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        backtrack(1, [])
        return res
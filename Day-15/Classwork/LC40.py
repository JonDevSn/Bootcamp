class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def backtrack(remain: int, start: int, path: list[int]):
            if remain == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                backtrack(remain - candidates[i], i + 1, path)
                path.pop()

        backtrack(target, 0, [])
        return res
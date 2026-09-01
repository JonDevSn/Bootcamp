class Solution:
    def printGraph(self, V: int, edges: list[list[int]]) -> list[list[int]]:
        adj = [[] for _ in range(V)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        return adj 
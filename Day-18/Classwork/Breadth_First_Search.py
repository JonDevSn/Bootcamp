from collections import deque


def bfs(graph: dict[str, list[str]], start: str) -> list[str]:
    """Breadth-First Search (BFS) traversal of a graph.

    Time Complexity:  O(V + E)
    Space Complexity: O(V)
    """
    visited = set([start])
    queue = deque([start])
    traversal_order = []

    while queue:
        node = queue.popleft()
        traversal_order.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order


# Example Usage:
# Graph:
#      A
#    /   \
#   B     C
#  / \     \
# D   E     F

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": [],
}

print(bfs(graph, "A"))
# Output: ['A', 'B', 'C', 'D', 'E', 'F']
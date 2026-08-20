class Solution(object):
    def binaryTreePaths(self, root):
        ans = []

        def dfs(node, path):
            if node is None:
                return

            path.append(str(node.val))

            # If leaf node
            if node.left is None and node.right is None:
                ans.append("->".join(path))
            else:
                dfs(node.left, path)
                dfs(node.right, path)

            # Backtracking
            path.pop()

        dfs(root, [])

        return ans
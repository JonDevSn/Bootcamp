class Solution(object):
    def pathSum(self, root, targetSum):

        ans = []

        def dfs(node, target, path):
            if node is None:
                return

            # Add current node to the path
            path.append(node.val)

            # Check if it is a leaf node
            if node.left is None and node.right is None:
                if node.val == target:
                    ans.append(path[:])

            else:
                # Search left and right
                dfs(node.left, target - node.val, path)
                dfs(node.right, target - node.val, path)

            # Backtracking
            path.pop()

        dfs(root, targetSum, [])

        return ans
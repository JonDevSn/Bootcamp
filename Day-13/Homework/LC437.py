class Solution(object):
    def pathSum(self, root, targetSum):

        prefix = {0: 1}

        def dfs(root, current_sum):
            if root is None:
                return 0

            current_sum += root.val

            count = prefix.get(current_sum - targetSum, 0)

            prefix[current_sum] = prefix.get(current_sum, 0) + 1

            count += dfs(root.left, current_sum)
            count += dfs(root.right, current_sum)

            prefix[current_sum] -= 1

            return count

        return dfs(root, 0)
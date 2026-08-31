class Solution(object):
    def maxPathSum(self, root):

        ans = [float('-inf')]

        def solve(root):

            if root is None:
                return 0

            left_gain = max(0, solve(root.left))
            right_gain = max(0, solve(root.right))

            current = root.val + left_gain + right_gain

            ans[0] = max(ans[0], current)

            return root.val + max(left_gain, right_gain)

        solve(root)

        return ans[0]
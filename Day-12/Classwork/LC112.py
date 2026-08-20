class Solution(object):
    def hasPathSum(self, root, targetSum):

        if root is None:
            return False

        # If we reach a leaf node
        if root.left is None and root.right is None:
            return root.val == targetSum

        # Subtract current value and continue
        targetSum -= root.val

        return (
            self.hasPathSum(root.left, targetSum) or
            self.hasPathSum(root.right, targetSum)
        )
class Solution(object):
    def minDepth(self, root):

        if root is None:
            return 0

        # Leaf node
        if root.left is None and root.right is None:
            return 1

        # No left subtree
        if root.left is None:
            return 1 + self.minDepth(root.right)

        # No right subtree
        if root.right is None:
            return 1 + self.minDepth(root.left)

        # Both subtrees exist
        return 1 + min(
            self.minDepth(root.left),
            self.minDepth(root.right)
        )
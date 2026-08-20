class Solution(object):
    def isBalanced(self, root):

        def height(node):
            if node is None:
                return 0

            leftHeight = height(node.left)
            rightHeight = height(node.right)

            # If any subtree is already unbalanced
            if leftHeight == -1 or rightHeight == -1:
                return -1

            # Check current node
            if abs(leftHeight - rightHeight) > 1:
                return -1

            return 1 + max(leftHeight, rightHeight)

        return height(root) != -1
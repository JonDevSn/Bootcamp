class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        def height(node):
            if node is None:
                return 0

            leftHeight = height(node.left)
            rightHeight = height(node.right)

            # Diameter passing through this node
            self.diameter = max(
                self.diameter,
                leftHeight + rightHeight
            )

            # Return height of current subtree
            return 1 + max(leftHeight, rightHeight)

        height(root)
        return self.diameter
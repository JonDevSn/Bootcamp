class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

        if root is None:
            return None

        # If we find p or q
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # p and q are found in different subtrees
        if left and right:
            return root

        # Return whichever side found a node
        if left:
            return left

        return right
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        ans = []

        def solve(root):
            if root is None:
                return

            solve(root.left)
            ans.append(root.val)
            solve(root.right)

        solve(root)
        return ans
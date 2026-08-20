# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def solve(self,ans, root):
        if root is None:
            return

        ans.append(root.val)
        self.solve(ans, root.left)
        self.solve(ans , root.right)

    def preorderTraversal(self, root):
        ans = []
        self.solve(ans , root)
        return ans

    
from collections import deque

class Solution(object):
    def levelOrder(self, root):

        if root is None:
            return []

        queue = deque([root])
        ans = []

        while queue:
            level = []
            size = len(queue)

            for i in range(size):
                node = queue.popleft()

                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            ans.append(level)

        return ans
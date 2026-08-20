from collections import deque

class Solution(object):
    def rightSideView(self, root):

        if root is None:
            return []

        queue = deque([root])
        ans = []

        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.popleft()

                # Last node of this level
                if i == size - 1:
                    ans.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return ans
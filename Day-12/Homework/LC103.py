from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):

        if root is None:
            return []

        queue = deque([root])
        ans = []
        leftToRight = True

        while queue:

            size = len(queue)
            level = []

            for _ in range(size):
                node = queue.popleft()

                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            # Reverse alternate levels
            if not leftToRight:
                level.reverse()

            ans.append(level)

            # Change direction for next level
            leftToRight = not leftToRight

        return ans
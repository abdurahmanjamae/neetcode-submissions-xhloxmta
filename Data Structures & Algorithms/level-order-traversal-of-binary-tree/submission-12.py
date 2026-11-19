from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        res = []
        queue = deque([root])

        while queue:
            level = []

            # Process all nodes at the current level
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                # Add children for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Save the completed level
            res.append(level)

        return res

# Mental Cue: Queue → Process one level → Add children → Save level → Repeat.
# RT: O(n) - Each node is visited once.
# Space: O(n) - Queue and result can store up to n nodes.
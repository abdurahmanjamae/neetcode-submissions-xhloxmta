from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:  # If the tree is empty, return an empty list
            return []

        res = [] # Store the values of each level
        queue = deque([root]) # Initialize the queue with the root node

        while queue:
            level = [] # Store the values of all nodes at the current level

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
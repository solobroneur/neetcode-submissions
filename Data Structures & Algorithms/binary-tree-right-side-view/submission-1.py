# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = list()
        queue = collections.deque()

        if root:
            queue.append(root)

        while queue:
            right_side = None

            for i in range(len(queue)):
                current_node = queue.popleft()
                if current_node:
                    right_side = current_node
                    queue.append(current_node.left)
                    queue.append(current_node.right)

            if right_side:
                output.append(right_side.val)


        return output
        
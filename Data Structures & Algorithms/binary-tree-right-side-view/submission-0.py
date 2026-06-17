# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        tree = list()
        queue = collections.deque()

        if root:
            queue.append(root)

        while len(queue) > 0:
            level = list()

            for i in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left) 
                if curr.right:
                    queue.append(curr.right)

            tree.append(level)

        output = list()

        for i in range(len(tree)):
            level = tree[i]
            last_node = level.pop()
            output.append(last_node)


        return output
        
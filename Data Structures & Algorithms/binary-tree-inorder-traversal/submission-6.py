# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.output = list()

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root)
        return self.output

    def traverse(self, node):
        if not node:
            return None

        self.traverse(node.left)
        self.output.append(node.val)
        self.traverse(node.right)
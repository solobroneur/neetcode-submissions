# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Store array for traversed node values
        output = list()

        # Algo to search the BST
        def inorder(node):
            if not node:
                return None

            inorder(node.left)
            output.append(node.val)
            inorder(node.right)

        # Start traversal
        inorder(root)

        # Return array
        return output
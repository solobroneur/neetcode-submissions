# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_node = TreeNode(preorder[0])
        middle_idx = inorder.index(preorder[0])

        # Build tree
        preorder_left = preorder[1:middle_idx + 1]
        preorder_right = preorder[middle_idx + 1:]

        inorder_left = inorder[:middle_idx]
        inorder_right = inorder[middle_idx + 1:]

        root_node.left = self.buildTree(preorder_left, inorder_left)
        root_node.right = self.buildTree(preorder_right, inorder_right)

        # return root node
        return root_node

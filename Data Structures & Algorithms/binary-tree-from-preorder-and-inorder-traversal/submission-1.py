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
        root_node.left = self.buildTree(preorder[1 : middle_idx + 1], inorder[:middle_idx])
        root_node.right = self.buildTree(preorder[middle_idx + 1 :], inorder[middle_idx + 1 :])

        # return root node
        return root_node

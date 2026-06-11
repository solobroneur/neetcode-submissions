# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 1. Base case: Check for empty BST / Recursion guard
        if not root:
            return None

        # 2. Search & Delete
        # Keep searching smaller
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        # Keep searching larger
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        # Node found
        else:
            # If node has 0 or 1 children
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # Node has 2 children
            else:
                # Replace with minimum val
                minimum_node = self.findMinimumNode(root.right)
                root.val = minimum_node.val
                # Remove subtree
                root.right = self.deleteNode(root.right, minimum_node.val)

        # 3. Return BST
        return root

    def findMinimumNode(self, root: Optional[TreeNode]):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

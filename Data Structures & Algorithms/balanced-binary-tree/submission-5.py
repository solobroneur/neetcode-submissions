# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node) -> [bool, int]:
            if not node:
                return [True, 0]

            left, right = dfs(node.left), dfs(node.right)
            left_balanced, left_height = left[0], left[1]
            right_balanced, right_height = right[0], right[1]
            node_balanced = abs(left_height - right_height) <= 1

            is_balanced = left_balanced and right_balanced and node_balanced
            return [is_balanced, 1 + max(left_height, right_height)]

        is_balanced, height = dfs(root)
        return is_balanced
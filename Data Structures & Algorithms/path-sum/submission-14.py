# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, current_sum):
            if not node:
                return False

            current_sum += node.val

            is_leaf_node = not node.left and not node.right
            is_sum_equal = current_sum == targetSum

            if is_leaf_node:
                return is_sum_equal
            if dfs(node.left, current_sum):
                return True
            if dfs(node.right, current_sum):
                return True

            return False

        return dfs(root, 0)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if(root is None):
            return True

        isBalanced = True

        def dfs(node, depth):
            nonlocal isBalanced
            if(node is None):
                return depth
            leftd = dfs(node.left, depth + 1)
            rightd = dfs(node.right, depth + 1)
            if abs(leftd - rightd) > 1:
                isBalanced = False
            return max(leftd, rightd)

        dfs(root, 0)
        return isBalanced
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        
        def dfs(node, maxP):
            nonlocal count
            if(node is None):
                return
            
            if(node.val >= maxP):
                count += 1
                maxP = node.val
            
            dfs(node.left, maxP)
            dfs(node.right, maxP)
        
        dfs(root, -101)
        return count
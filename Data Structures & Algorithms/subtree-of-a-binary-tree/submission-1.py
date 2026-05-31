# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(root, subroot):
            if(root == None):
                return False
            if(subroot == None):
                return True
            if(root.val == subroot.val):
                if(samedfs(root, subroot)):
                    return True
            left = dfs(root.left, subroot)
            right = dfs(root.right, subroot)
            return left or right

        def samedfs(p, q):
            if(p == None and q == None):
                return True
            if(p == None or q == None):
                return False
            if(p.val != q.val):
                return False
            
            left = samedfs(p.left, q.left)
            right = samedfs(p.right, q.right)
            return left and right

        return dfs(root, subRoot)
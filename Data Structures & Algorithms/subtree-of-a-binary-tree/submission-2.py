# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if(root is None):
            return False

        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot))

    def sameTree(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        if((r1 is None) ^ (r2 is None)):
            return False
        elif(r1 is None and r2 is None):
            return True
        else:
            if(r1.val == r2.val):
                return self.sameTree(r1.left, r2.left) and self.sameTree(r1.right, r2.right)
            else:
                return False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, lv, rv):
            if(root is None):
                return True
            if(lv >= root.val or rv <= root.val):
                return False
            check_left = valid(root.left, lv, root.val)
            check_right = valid(root.right, root.val, rv)
            return check_left and check_right
        return valid(root, float('-inf'), float('inf'))
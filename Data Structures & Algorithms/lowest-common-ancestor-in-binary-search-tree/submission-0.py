# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def lcs(root, p, q):
            if(root == None):
                return None
            if(root.val > p.val and root.val > q.val):
                return lcs(root.left, p, q)
            if(root.val < p.val and root.val < q.val):
                return lcs(root.right, p ,q)
            else:
                return root

        return lcs(root, p, q)
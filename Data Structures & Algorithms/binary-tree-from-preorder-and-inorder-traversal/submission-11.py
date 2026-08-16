# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mymap = {v: i for i, v in enumerate(inorder)}
        i = 0

        def tree( l, r):
            nonlocal i
            if(r < l):
                return None
            
            root = TreeNode(preorder[i])
            i += 1
            mid = mymap[root.val]
            root.left = tree(l, mid - 1)
            root.right = tree(mid + 1, r)
            return root

        return tree(0, len(inorder) - 1)
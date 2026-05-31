class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def dfs(root):
            if root is None:
                return
            dfs(root.left)          # visit left first
            res.append(root.val)    # then current node
            dfs(root.right)         # then right

        dfs(root)
        return res[k - 1]

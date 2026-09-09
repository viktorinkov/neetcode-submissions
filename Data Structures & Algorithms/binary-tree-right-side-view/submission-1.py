# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # do bfs
        # for each layer pick the last element

        q = deque()
        if root is None:
            return []
        q.append(root)
        res = []
        curr = None

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if(curr.left is not None):
                    q.append(curr.left)
                if(curr.right is not None):
                    q.append(curr.right)

            res.append(curr.val)

        return res

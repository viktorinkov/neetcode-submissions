# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root is None):
            return []
        res = []
        my_queue = collections.deque()
        my_queue.append(root)
        while my_queue:
            n = len(my_queue)
            level = []
            for i in range(n):
                curr = my_queue.popleft()
                if(curr):
                    level.append(curr.val)
                    my_queue.append(curr.left)
                    my_queue.append(curr.right)
            if level:
                res.append(level)

        return res

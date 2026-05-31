# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        def dfs(root):
            nonlocal res
            if(root is not None):
                res += str(root.val)
                res += ","
                dfs(root.left)
                dfs(root.right)
            else:
                res += "N,"
        
        dfs(root)
        return res


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        dataAsArr = data.split(',')
        idx = 0
        def dfs():
            nonlocal idx
            if(dataAsArr[idx] == "N"):
                idx += 1
                return None
            else:
                node = TreeNode(int(dataAsArr[idx]))
                idx += 1
                node.left = dfs()
                node.right = dfs()
                return node

        return dfs()




        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #bfs problem: 

        res = []
        def bfs(root):
            queue = [root]
            while (queue):
                level_size = len(queue)
                level = []
                for i in range(level_size): 
                    current = queue.pop(0)
                    level.append(current.val)
                    if (current.left): 
                        queue.append(current.left)
                    if (current.right): 
                        queue.append(current.right)
                res.append(level)
        if root is None: 
            return res
        else: 
            bfs(root) 
        return res


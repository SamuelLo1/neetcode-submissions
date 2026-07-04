# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #just perform a dfs on both trees, if they return the same sequence then return true
        self.sameTree = True
        def dfs(p,q): 
            
            if not self.sameTree: 
                return 
            if p is None and q is None: 
                return 
            elif p is None or q is None: 
                self.sameTree = False
                return

            dfs(p.left,q.left)
            dfs(p.right,q.right)

            if(p.val != q.val): 
                self.sameTree = False
                return 
        dfs(p,q)
        return self.sameTree
            
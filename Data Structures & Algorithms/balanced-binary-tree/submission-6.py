# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """

        """
        self.unbalanced = False 
        def dfs(root): 
            if not root or self.unbalanced:
                return 0 
            

            left = dfs(root.right)
            right = dfs(root.left)

            if (left > (right + 1) or right > (left + 1)): 
                self.unbalanced = True
            
            return max(left, right) + 1
        
        dfs(root)
        return not self.unbalanced

        
        
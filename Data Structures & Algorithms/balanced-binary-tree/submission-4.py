# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        the tree is balanced if subtrees of every node differ by no more than 1
        """
        
        #left and right subtrees differ by height no more than 1
        #do a bottom up approach
        #checking at each node if it is balanced continue
        #else return false
        #get the height of left and right subtree and make a comparison, return false if one subtree's height greater than other's height by 1
        #break out of recursion when the case is found

        self.balanced = True
        def dfs (node): 
            if node is None: 
                return 0


            leftHeight = dfs(node.left)        
            rightHeight = dfs(node.right)
            if abs(leftHeight - rightHeight) > 1: 
                self.balanced = False
            return 1 + max(leftHeight,rightHeight) 


        dfs(root)
        return self.balanced
        
        
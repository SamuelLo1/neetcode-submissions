# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    """
    binary tree
    
    ex) 

    dfs: 
    [1,3,7,6,2,5,4]
    then do a dfs traversal on the whole graph popping from the stack use the nodes from the stack popped
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root: 
            return None
        
        #this swaps at each level
        root.left, root.right = root.right, root.left
        
        #do dfs()
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

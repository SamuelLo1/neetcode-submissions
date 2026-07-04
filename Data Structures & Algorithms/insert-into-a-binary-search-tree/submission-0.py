# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        interesting thing about bst: 
        can just traverse and insert, don't need to worry about deforming a bst.
        try to look for clever patterns / rules to work off of. 
        """
        # create new node to insert
        new_node = TreeNode()
        new_node.val = val
        # not root case
        if not root: 
            return new_node

        #can only be inserted as leaf node
        def dfs(root): 
            if not root: 
                return new_node

            # want one of these to resolve    
            if val > root.val: 
                root.right = dfs(root.right)
            else:
                root.left = dfs(root.left)

            # want root to resolve after the root.right is set or root.left
            return root

        return (dfs(root))

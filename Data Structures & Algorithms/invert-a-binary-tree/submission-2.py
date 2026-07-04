# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
binary tree not necessarily balanced
edit existing binary tree
will want to use some kind of swapping
return root


each parent would swap nodes, 
then the parents above would then swap
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        # each parent swaps left and right can just do simple dfs
        original = root
        def dfs(root): 
            if not root: 
                return 
            # if there is a left and right swap
            print("root", root.val)

            root.left, root.right = root.right, root.left

            
            left_val = -1 if not root.left else root.left.val 
            right_val = -1 if not root.right else root.right.val
            print("swapped", left_val, right_val)
            dfs(root.left)
            dfs(root.right)

            return root

        root = dfs(root)
        return root
    
 
        
            
            
      

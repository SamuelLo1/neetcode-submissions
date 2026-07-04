# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- left subtree contains only nodes less than current node's key
- right subtree contains only nodes greater than node's curr key

- at each node update a bounds. 
- left bound is updated if key is less than 
- right bound is updated if key is greater than 

- drew out bigger example to visualize 
- there is boundary

starting bounds: [1, 2]
    - go left: update right
    - go right: update left
first right: 
[-inf, 2] [4,inf] [2, 4]
        4
    2.      5
1      3
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.validBST = True
        def dfs(root, left_b, right_b): 
            if not root: 
                return 
            
            if not self.validBST: 
                return False
            
            if not (left_b < root.val and right_b > root.val):
                print(root.val, left_b, right_b) 
                self.validBST = False
                return False
            
            dfs(root.left, left_b, root.val)
            dfs(root.right, root.val, right_b)            

            return True
        dfs(root, float('-inf'), float('inf'))
        return self.validBST


        
        



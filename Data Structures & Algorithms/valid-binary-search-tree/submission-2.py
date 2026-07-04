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
        # dfs 
        def dfs(root, bounds): 
            if (not root): 
                return True

            # checking bounds
            if ((bounds[0] >= root.val) or (bounds[1] <= root.val)):
                print(bounds, root.val)
                return False
            
            # update bounds for left
            left_rec_bounds = bounds.copy()
            left_rec_bounds[1] = root.val
            # end as soon as false is returned
            if not (dfs(root.left, left_rec_bounds)):
                return False
            
            # end as soon as false is returned
            right_rec_bounds = bounds.copy()
            right_rec_bounds[0] = root.val
            if not (dfs(root.right, right_rec_bounds)):
                return False
            
            return True
        
        if (dfs(root, [-1001,1001])):
            return True
        return False

        
        



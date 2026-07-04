# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #run a dfs on the left and right and add both of the trees together
        self.res = 0 


        def dfs(node):
            if node is None: 
                return 0
            
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            #the max can be found by taking the max of the left and right subtree
            #calculate the maximum bottom up
            self.res = max(self.res, leftMax + rightMax)
            #returning the max distance for each node
            return 1 + max(leftMax,rightMax)

        dfs(root)
        return self.res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # root node is good
        # along a path use dfs, can keep track of a greatest seen
        # if curr is greater than greatest seen then aggregate count
        self.num_good_nodes = 0
        
        def dfs(root, prev_good): 
            if (not root): 
                return 
            
            curr_good = prev_good
            if (prev_good <= root.val): 
                curr_good = root.val
                self.num_good_nodes += 1

            dfs(root.left,curr_good)
            dfs(root.right,curr_good)

            return 

        dfs(root, -101)
        return self.num_good_nodes
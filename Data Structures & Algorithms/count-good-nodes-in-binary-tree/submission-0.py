# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #dfs if next node is greater than or equal to current node inc global count
        #for each branch keep track of a max, if the current value is greater than the max, increment
        self.good_nodes = 0
        def dfs(root,greatest): 
            if root is None: 
                return
            
            if root.val >= greatest: 
                self.good_nodes += 1
                greatest = root.val
            
            dfs(root.left, greatest)
            dfs(root.right, greatest)

        dfs(root, float("-inf"))
        return self.good_nodes

        
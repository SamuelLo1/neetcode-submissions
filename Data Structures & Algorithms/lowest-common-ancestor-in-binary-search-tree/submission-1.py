# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
all node values unique
given p and given q, return lowest common ancestor
ancestor is allowed to be descendent


start from root, 
 - benefits of a bst: 
    - if root in between p and q, return root
    traverse the side where p and q both 
    - recursive relation: 
        - find a value such that between p and q, 
        - if no such value and first value we come across 
        is p or q, return 



"""
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.LCA = root

        #go through each node of the tree to try to find value that works 
        def dfs(root): 
            if not root: 
                return 

            if (p.val <= root.val <= q.val) or (q.val <= root.val <= p.val ): 
                self.LCA = root
                return 
            dfs(root.right)
            dfs(root.left)
            return

        dfs(root)
        return self.LCA
            #check value between p and q

        
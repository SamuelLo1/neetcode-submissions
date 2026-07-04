# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #all values are unique, return LCA, ancestor can be the same descendent


        #dfs traversal, can start returning when both of the nodes are found. 
        #top down approach. 
        #can return when both nodes are found. 
        self.lowestCommon = root
        self.commonFound = None
        self.larger = 0
        self.smaller = 0


        #trace till both are found and return up the stack when they are found
        def dfs(root): 
            if root is None or self.commonFound: 
                return 

            #if the current node is less than p and q, search the right subtree
            #else search left subtree
            if root.val >= self.smaller and root.val <= self.larger : 
                print(root.val)
                self.commonFound = root
                return 
            #root is less than smaller
            elif root.val <= self.smaller: 
                dfs(root.right)
            else: 
                dfs(root.left)
            

            

        #take the larger value first: 
        if (p.val > q.val): 
            self.smaller = q.val
            self.larger = p.val
        else: 
            self.smaller = p.val 
            self.larger = q.val 

        print(self.smaller,self.larger)

        dfs(root)

        return self.commonFound

            
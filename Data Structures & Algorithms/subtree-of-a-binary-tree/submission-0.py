# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #can dfs through the root and subtree only if the root value can be matched
        #all of descendents must be the same, should have looked through the example 
        self.trees_equal = False

        def dfs(root, subroot):
            if root is None or self.trees_equal: 
                return 
            #run a check to see if subtree exists
            if root.val == subroot.val: 
                if (check_tree_equal(root,subroot)):
                    self.trees_equal = True
                    return
            print(root.val)
            dfs(root.left, subroot)
            dfs(root.right,subroot)

            return

        def check_tree_equal(root, subroot):
            #both terminate at the same time 
            if subroot is None and root is None: 
                return True
            #only one of them are None, they are not equal
            elif root is None or subroot is None:
                return False
            print(root.val, subroot.val)
            if (root.val != subroot.val):
                return False
            leftFlag = check_tree_equal(root.left, subroot.left)
            rightFlag = check_tree_equal(root.right,subroot.right)

            return (leftFlag and rightFlag)

        #if they don't exist: 
        # if root is None and subroot is None:
        #     return True
        # else: 
        #     return False 


        dfs(root,subRoot)
        return self.trees_equal 
            
            
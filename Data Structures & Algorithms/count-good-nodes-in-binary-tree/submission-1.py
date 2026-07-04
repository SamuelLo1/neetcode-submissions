# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # good node if path from root to node contains no node greater than value of x
        # can dfs and keep track of a max node in path. 
        # mark nodes as good nodes

        # aggregate the good nodes
        def dfs(root, path_max):  
            # base condition: 
            if (root is None): 
                return 0
            
            is_good_node = 0
            if (root.val >= path_max): 
                is_good_node = 1
                path_max = root.val

            good_left = dfs(root.left, path_max)
            good_right = dfs(root.right, path_max)

            return good_left + good_right + is_good_node
        
        return dfs(root,-101)
        
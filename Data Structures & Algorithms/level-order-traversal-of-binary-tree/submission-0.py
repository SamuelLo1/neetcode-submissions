# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #bfs problem: 

        #dictionaries maintin insertion order past python 3.7 so I can just turn this dictionary into list after
        node_levels = []
        def bfs(root):
            queue = [(root,0)]
            while queue: 
               current, level = queue.pop(0)
               add_to_array(current.val, level)
               if (current.left): 
                    queue.append((current.left, level + 1))
               if (current.right): 
                    queue.append((current.right, level + 1))
            
        
        def add_to_array(node_value, node_level):
            #first node
            if (node_level == 0): 
                node_levels.append([node_value])
                return
            #check if subarray exists if not make one
            if (len(node_levels) - 1) - node_level == 0: 
                node_levels[node_level].append(node_value)
                return
            else: 
                node_levels.append([node_value])
                return
        
        if root is None: 
            return node_levels

        bfs(root)
        return node_levels

            
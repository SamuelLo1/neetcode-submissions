# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #get use a bfs to go to the last level
        # a tree is always connected and acyclic so the largest layer is the greatest depth
        max_dist = 0
        if root is None: 
            return max_dist


        queue = [(root,1)]
        while(queue): 
            current, current_dist = queue.pop(0)
            max_dist = max(max_dist, current_dist)
            if (current.left): 
                queue.append((current.left, current_dist + 1))
            
            if (current.right): 
                queue.append((current.right, current_dist + 1))

        return max_dist

        
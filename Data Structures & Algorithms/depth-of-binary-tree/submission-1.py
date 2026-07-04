# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root: 
            return 0
        self.maxHeight = 0
        queue = [root]
        #use a for loop to keep track of level per level
        while queue: 
            for i in range(len(queue)): 
                currNode = queue.pop(0)
                if currNode.right:
                    queue.append(currNode.right)
                if currNode.left: 
                    queue.append(currNode.left)
            self.maxHeight = self.maxHeight + 1
        return self.maxHeight
        

        
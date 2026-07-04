# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        """
        delete all leaf nodes with value of target
        recursive behavior, if prev leaf nodes get 

        do in-order traversal to get leaf nodes
        return none when target is found and it is leaf node 

        """

        if not root: 
            return None
        
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if (not root.right) and (not root.left) and (root.val == target): 
            return None
        else: 
            return root

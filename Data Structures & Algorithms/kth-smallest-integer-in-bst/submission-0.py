# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        given bst
        find kth smallest value 

        brute force : traverse the tree, sort all elements get the kth element

        another method : useful to know how many nodes on the left or right to a node
        post order traversal ? 

        introducing another ds : heap? 

        can do a post order traversal, and toss elements into a heap
        """ 
        self.counter = 0 
        self. kth_element = -1 
        def dfs(root):

            if not root: 
                return 
            dfs(root.left)

            self.counter += 1
            if self.counter == k: 
                self.kth_element = root.val

            dfs(root.right)

        dfs(root)

        return self.kth_element

        


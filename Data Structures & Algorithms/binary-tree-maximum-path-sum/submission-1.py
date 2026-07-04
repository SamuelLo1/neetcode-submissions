# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Intuition: 
        - max path sum 
        - would need to compute the sum at each node: 
        
        Thoughts: 
        - as long as nodes are connected, they can be part of same path
        - greedy? 
        - keep in mind only need to keep track of a max sum 
        - Does traversal matter? 
            - bfs traversal? 
            - whilst positive, 
        - can think in terms of if a subtree is increasing or decreasing
        - any kind of traversal but add it up. 
        - if the subtrees are increasing, positive, then add it, else 
        - if the subtrees are decreasing ignore it : choosing to include subtree or not
        - whenever returning a value, update max 
        

        - maybe can prioritize positive
            - can skip negatives 
            - can add through negatives (include in sum)
        - Can I turn this into diff data struct? 
            - 
        - what kind of traversals
            - postorder 
            - 
        """
        self.max_path_sum = float('-inf')

        def dfs(root):
            if not root: 
                return 0 
            
            left_subtree_sum = dfs(root.left)
            right_subtree_sum = dfs(root.right)

            max_possible_value = max(
                left_subtree_sum + root.val, 
                right_subtree_sum + root.val, 
                left_subtree_sum + right_subtree_sum + root.val, 
                root.val
            )

            self.max_path_sum = max(self.max_path_sum, max_possible_value)
            return max(root.val, root.val + left_subtree_sum, root.val + right_subtree_sum)
        
        dfs(root)
        return self.max_path_sum
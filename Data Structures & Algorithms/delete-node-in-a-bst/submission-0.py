# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Find node 
delete node

5,3,9,1,4

can return any tree after deletion
to find a node in bst, 
larger then go right, lesser then go right 

if found the node, then delete. 
deleteNode()

in recursion always thinking: 
what is the next action I want to take. 
Its like a series of actions I want to engrain

Can think of this as replacing the previous nodes

# key to note that dfs still has O(N) worst time complexity for bfs
# but average time complexity is log(N) -- log base 2
"""
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: 
            return root 

        if key > root.val: 
            root.right = self.deleteNode(root.right, key)
        elif key < root.val: 
            root.left = self.deleteNode(root.left, key)
        else: 
            print("deleting a node")
            # equal than 
            if not root.left: 
                return root.right 
            elif not root.right: 
                return root.left 

            # get right of current node and leftmost value 
            cur = root.right
            print(cur.val)
            while cur.left: 
                cur = cur.left 
            
            cur.left = root.left 
            print(cur.left.val)
            res = root.right
            print(res.val)
            del root

            return res
        
        return root 



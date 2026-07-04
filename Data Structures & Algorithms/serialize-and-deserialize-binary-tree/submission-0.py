# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    """
    if I do dfs on a node: I can reconstruct it from dfs aswell? 
    the issue is null nodes  

    
    """
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # do pre-order traversal for good formatting: 
        # root -> left_subtree -> right_subtree
        # if encounter a None node return "N"
        res = []
        def dfs(root): 
            if not root: 
                res.append("N")
                return 
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # have an index to loop through the string
        # index should be handled globally, should not be handled locally
        # incremend if we encounter "N"
        print(data)
        arr = data.split(",")
        self.i = 0
        # base case
        if arr[0] == "N": 
            return None
        def dfs(): 
            # need to incremenet, create node, attach left and right subtree 
            if (arr[self.i] == "N"):
                self.i += 1
                return None
            new_node = TreeNode(arr[self.i])
            self.i += 1
            new_node.left = dfs()
            if (new_node.left):
                print(new_node.left.val, self.i)
            new_node.right = dfs()
            if (new_node.right):
                print(new_node.right.val, self.i)


            return new_node
        return dfs()


            



        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #at each level add the right-most element: 
        #can create a list at each 
        #run bfs and get the right-most element in the queue at all times
        
        right_most = []
        def bfs(root): 

            #each time the queue is populated get the leftmost element 
            queue = [root]
            while queue: 
                level_len = len(queue)
                right_most.append(queue[-1].val)
                #for each node in the level add children to queue
                for i in range(level_len): 
                    current = queue.pop(0)
                    if (current.left): 
                        queue.append(current.left)
                    if (current.right): 
                        queue.append(current.right)


        if root is None: 
            return right_most
            
        bfs(root)
        return(right_most)
                    

                    


                



                #rightMost is the             
            
        
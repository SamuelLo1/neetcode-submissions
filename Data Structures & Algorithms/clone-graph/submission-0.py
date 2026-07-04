"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        connected, undirected 
        deep copy of graph

        each node contains val and list of neighbors
        adj  {node : neighbors}

        nodes numbered 1 - n 
        Given adjList, form a deep copy of graph 
        adj list is indeces and the nodes each index is connected to

        at each level of recursion can create a node with all its neighbors
        when I traverse dfs to a node can populate a node, 
        can store created nodes in a set so that they can be used as neighbor nodes
        """
        if (node is None): 
            return None

        copy_nodes = {}

        # recursively create a copy node and add in neighbors of copynodes 
        # recursion stack should return to root node with fully formed graph
        def dfs(root): 
            if (root.val in copy_nodes):
                return copy_nodes[root.val]

            copy = Node(root.val) 
            copy_nodes[root.val] = copy
            
            for neighbor in root.neighbors: 
                copy.neighbors.append(dfs(neighbor))
            
            return copy

        return dfs(node)


                

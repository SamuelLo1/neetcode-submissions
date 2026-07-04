class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        any graph w/o simple cycles is tree. 
        undirected edges 

        nodes labeled 0 - (n- 1)
        array of n - 1 edges
        each edge contains (a[i], b[i]) undirected

        can choose any node as root. 
        choosing a specific x will minimize height 
        return a list of all minimum heigh labels

        minimum height is longest path from root to any node  
        
        want node in middle? 
        node with lots of edges? 

        brute force: pick each node and test the distance 
        can use dfs to get distance 
        and traverse the graph from edges. 
        
        how to get longest path in tree, explore every edge brute force each time and calculate distance
        from root to a leaf node when encountered. leaves only have 1 reference. 
        O(V * (V + E))

        can keep pruning until there are no more leaf nodes
        leaf node properties: only one neighbor 
        so would edit an adj list each time 

        no cycles can exist so no need to worry about n > 2 
        """
        if n == 1: 
            return [0]
        
        # form adj list: 
        adj = {}
        for u , v in edges: 
            if (u in adj): adj[u].add(v)
            else: adj[u] = set([v])
            if (v in adj): adj[v].add(u)
            else: adj[v] = set([u])

        # recursively prune leaf nodes: 
        # will edit the adj list 
        # bfs for pruning, prune level at a time

        # get initial leaf nodes: 
        q = deque()
        for node, neighbors in adj.items(): 
            if len(neighbors) == 1: 
                q.append(node)
        # for pruning need to prune level at a time
        # bfs pruning
        remaining_nodes = len(adj)

        while remaining_nodes > 2: 
            leaves_length = len(q)
            for _ in range(leaves_length): 
                # base case 
                curr = q.popleft()
                # for each neighbor, update the adj list and queue up nodes
                for neigh in adj[curr]: 
                    adj[neigh].remove(curr)
                    if len(adj[neigh]) == 1: 
                        q.append(neigh)

                # prune the curr node
                del adj[curr]
                remaining_nodes -= 1

        # form all the keys in adj into an array
        res = []
        for node in adj.keys(): 
            res.append(node)
        return res
                



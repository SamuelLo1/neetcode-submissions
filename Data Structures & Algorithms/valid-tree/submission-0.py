class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        given 0 to n - 1 
        check whether nodes make a valid tree 

        valid tree means that there are no cycles and connected

        if I can dfs from one node to all other nodes and 
        if I don't visit same edge more than once, I am good 

        {
            0: [1,2,3]
            1: [0,4]
            2: [0]
            3: [0]
            4: [1]        
        }
        visited = 0,1,2,3,4


        can go from 0 1 goes to 4
        can go from 0 to 2 and 0 to 3 
        
        how to detect cycles in undirected graph
        in dfs(keep track of parent, curr, visited)

        {
        0: 
        }
        """
        if (len(edges) == 0): 
            return True

        graph = defaultdict(list)
        for u,v in edges: 
            graph[u].append(v)
            graph[v].append(u)
        
        self.contains_cycle = False 
        visited = set()
        # should contain a visited set. 
        # if a node is visited more than once then exit 
        def dfs(prev,curr): 
            print("inside dfs")
            # cycle detected
            if (curr in visited): 
                print("loop found", curr)
                return False

            visited.add(prev)
            for neigh in graph[curr]: 
                if neigh != prev: 
                    if(not dfs(curr, neigh)):
                        return False

            visited.add(curr)
            return True 
                        

        init_u ,_ = edges[0]
        # loop through all initial edges connected
        for neigh in graph[init_u]: 
            if not (dfs(init_u, neigh)): 
                return False
    
        print(visited)
        if not self.contains_cycle and len(visited) == n: 
            return True
        else: 
            return False






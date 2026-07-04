class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        given heights, 
        water can flow from 

        water can flow four directions 
            - flows to cells with equal or lower amt
            maybe have some sense of pacific side 
            some sense of atlantic side of ocean 

        Plan: 
        - get all tiles that are related to the pacific ocean 
        - get all tiles that are related to the atlantic ocean 

        - find intersecting between the sets
        - if cells are visited, then do not visit again. 
        """


        pacific_visited, atlantic_visited = set(), set() # sets would store elements (x,y) tups 
        # do dfs for faster code. bfs would require q, no need for bfs
        n = len(heights)
        m = len(heights[0])
        # add new cells to visited and cells that are candidates
        def dfs( coord, visited ):
            x, y = coord
            # base case
            if coord in visited: 
                return 
            visited.add(coord)
            # explore neighbors
            for dx, dy in [[-1,0], [1,0], [0,1], [0,-1]]: 
                # conditions before continuing dfs 
                new_x = dx + x
                new_y = dy + y
                if ((new_x) >= 0 and 
                    (new_x) < n and
                    (new_y) >= 0 and 
                    (new_y) < m and # within bounds
                    heights[new_x][new_y] >= heights[x][y] # only explore if all conditions are met
                ):
                    dfs((new_x,new_y), visited)

        # for all pacific cells run dfs
        for i in range (m): 
            dfs((0,i), pacific_visited)
        for j in range (n): 
            dfs((j,0), pacific_visited)

        # for all atlantic cells run dfs
        for k in range (m): 
            dfs((n - 1,k), atlantic_visited)
        for l in range (n): 
            dfs((l, m - 1), atlantic_visited)

        # get the intersection of pacific visited and atlantic_visited 
        res = []
        for coord in pacific_visited: 
            if coord in atlantic_visited: 
               res.append(coord) 

        return res




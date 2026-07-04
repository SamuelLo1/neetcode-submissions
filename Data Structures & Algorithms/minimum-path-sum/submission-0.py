class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        m x n grid filled with non-negative numbers
        find path from top left to bottom right. 
        minimizes sum of all numbers

        can only move down or right

        at each point you want to take the 
        """

        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for i in range(m)]
        dp[m-1][n-1] = grid[m-1][n-1]

        for i in range (m - 1, -1, -1): 
            for j in range(n - 1, -1, -1): 
                if (i == (m - 1) and j == (n - 1)): 
                    continue
                # handle edges
                if (i == m - 1): 
                    dp[i][j] = grid[i][j] + dp[i][j + 1]
                    continue
                if (j == n - 1):
                    dp[i][j] = grid[i][j] + dp[i+1][j]
                    continue

                dp[i][j] = min(dp[i + 1][j] , dp[i][j + 1]) + grid[i][j]
        
        return dp[0][0]
                


                        


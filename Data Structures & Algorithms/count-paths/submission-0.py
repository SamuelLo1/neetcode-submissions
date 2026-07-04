class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        return total number of paths from grid [0][0] to grid[m-1][n-1]

        can only move down or right at any time. 

        summing up right and bottom

        """

        dp = [[0] * n for i in range(m)]

        for i in range(m - 1, -1,-1): 
            for j in range(n - 1, -1, -1): 
                # base cases
                if i == m - 1: 
                    dp[i][j] = 1
                    continue
                if j == n - 1: 
                    dp[i][j] = 1
                    continue
                # compute dp 
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]



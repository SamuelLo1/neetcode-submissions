class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        


        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # if (obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1): 
        #     return 0 

        dp = [[0] * n for i in range(m)]
        dp[m-1][n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1): 

                # if there are obstacles then return 
                if obstacleGrid[i][j] == 1: 
                    dp[i][j] = 0
                    continue
                
                # skip the corner
                if i == m - 1 and j == n - 1: 
                    continue
                
                # edges have specific adding logic 
                if i == m - 1: 
                    dp[i][j] = dp[i][j + 1]
                    continue
                
                # edges have specific adding logic
                if j == n - 1: 
                    dp[i][j] = dp[i + 1][j]
                    continue

                # actual dp logic
                dp[i][j] = dp[i + 1][j] + dp [i][j + 1]

        return dp[0][0]
                

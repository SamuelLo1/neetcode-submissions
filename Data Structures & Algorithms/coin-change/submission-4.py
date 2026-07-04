class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        """
        Does the number of coins matter here? 
        
        coins : array of coins and an integer amount
        return fewest amount of coins needed to make up amount

        Questions: 
        - are negative coins allowed? 
        - 

        bfs? 
        - can start at one coin and try the rest, at the first instance that I can 
        - create the amount return the coin # 

        dfs
        - at each decision can choose any 1-n coins
        - can memoize at a specific coin number if I only need one coin to form to the sum
        -
        - use recursive calls to memoize the min of the coins needed. 
        """
        # cache size of amount
        dp = {}
        

        def dfs(value): 
            # basecase: if greater than or equal to target return 
            if (value == amount): 
                return 1 

            # checking cache
            if value in dp: 
                return dp[value]

            min_value = 1e9
            # recursion 
            for coin in coins: 
                if ((coin + value) <= amount ):
                    dfs_value = dfs(value + coin)
                    # making sure we get min value from recursion
                    min_value = min(min_value, 1 + dfs_value)
            # store and return value
            dp[value] = min_value
            return dp[value]

        res = dfs(0)
        return -1 if res >= 1e9 else res - 1







class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        get the number of distinct ways to make a value
        value of coins is unique 
        coins can be reused


        Thoughts: 
            - brute force: 
            - decision tree: 
            - at each decision can pick one number or the others (backtracking)
            - can memoize the backtracking algo: 

            Memoizing: 
            - for any coin amount and index (selected coin)
                can memoize how many ways to obtain amount 
            -  can go top-down recursion: 
                we accumulate the sum as we go
                
            memo: {(value): amt_of_successful_paths}
            a dp[value] is not concluded until we see all the branches 
            of the dp[value] and it is the sum of all the earlier possibilities


            Recursion: 
                - keep track :
                    - index 
                    - value
        """

        dp = {}

        def dfs(index, value):
            # 🎯 base cases
            if value == amount:
                return 1
            if value > amount or index >= len(coins):
                return 0

            # ✅ memo key should include both index and value
            if (index, value) in dp:
                return dp[(index, value)]

            total_ways = 0

            # the key is to make sure that we cannot add the same number back, 
            # once we have recursed it all possibilites have been found for it and when 
            # moving forward all subsequent indexes will be unique
            # ✅ loop only over remaining coins (to avoid permutation duplicates)
            for i in range(index, len(coins)):
                # ✅ reuse coin i by not incrementing it to i+1 automatically
                total_ways += dfs(i, value + coins[i])

            dp[(index, value)] = total_ways
            return total_ways

        return dfs(0, 0)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        can either add or subtract an element 
        return the diff ways to obtain target

        backtracking: 
            - keep track of sum
            - can choose to either add or subtract current element
            - base case is that we reach end of array check if the sum matches target: 
            - if so, then increment global count 

    
        dynamic programming: 
            - when I pick an operation -> want to know curr_sum and index if 
            how many ways to obtain target? can add one to the amount of ways to achieve from the memoized target
            - in backtracking add together the negative and positive cases into memo

            memo : { (curr_sum, index) : target_ways }
        """

        # define memo cache 
        memo = {} # {( curr_sum, index ) : target_ways }
        # define backtracking algo + memoization 
        #
        # iter 0: 
        #  iter 1 (-) 
        #  iter 1 (+)
        def dfs(index, curr_sum):
            
            # base case : reached len(nums) and equal to target sum, return 1 
            if (index == len(nums) and curr_sum == target): 
                return 1 

            if (index == len(nums)): 
                return 0

            if (index, curr_sum) in memo: 
                return memo[(index, curr_sum)]  

            # iterations of backtracking update curr_sum
            subtract_iter = dfs(index + 1, curr_sum - nums[index]) 
            add_iter = dfs(index + 1, curr_sum + nums[index])

            memo[(index, curr_sum)] = subtract_iter + add_iter
            return memo[(index, curr_sum)]
        
        return dfs(0,0)


            # return sums from iterations
        
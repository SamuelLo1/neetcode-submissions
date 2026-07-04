class Solution:

    """
        - return list of all unique combos of nums that sum to target
        - each num can be used unlimited
        - any order
        - backtracking: 
            - add all numbers first and if too high, 
    """
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        uniqueSums = []
        currNums = []
        nums.sort()


        #by going from start, we ensure that prev computed sums not reencountered
        def dfs(start): 
            currSum = sum(currNums)

            #out of bounds
            if (start == len(nums) or currSum > target): 
                return 

            if (currSum == target ): 
                uniqueSums.append(currNums[:])
                return

            for i in range(start, len(nums)):
                
                currNums.append(nums[i])
                dfs(i)
                currNums.pop()
                    

        dfs(0)
        return uniqueSums
            
            

            

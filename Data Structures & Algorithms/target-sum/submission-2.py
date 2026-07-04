class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        given array of integers

        return different ways can build expression: total sum equals taregt

        for each integer can either add or subtract
        2^n possibilities: 

        """
        def backtrack(i, total):
            if i ==len(nums):
                return  total == target
            
            return (backtrack(i + 1, total + nums[i]) + 
                    backtrack(i + 1, total - nums[i]))
                
        return backtrack(0, 0)
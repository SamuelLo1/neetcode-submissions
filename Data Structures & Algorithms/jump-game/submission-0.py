class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        can brute force decisions  
        from each index have the decision to jump to any of x <= nums[index]

        THoughts: 
            - subproblem: 
                - if I go in reverse and can calculate to the end.  
        """

        dp = [False] * len(nums)
        n = len(nums) - 1
        prev_marked_true = n
        for i in range (len(nums) - 1, -1,-1):
            
            if ((i + nums[i]) >= n or (i + nums[i]) >= prev_marked_true): 
                dp[i] = True
                prev_marked_true = i
                continue
        print(dp)
        return dp[0]
            

            

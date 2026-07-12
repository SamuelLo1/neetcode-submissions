class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        can either choose to rob a house or not rob a house
        - cannot rob adjacent houses
        - can calculate a maximum possible at any distance
        - at each i, consider the max between: memo[i-2] + nums[i], memo[i-1] 

        [1,1,3,3]
        memo : [1,1,4,4]

        [2,9,8,3,6]
        memo: [2,9,10,12,16]
        """ 
        n = len(nums)
        for i in range(n):
            # ensure i is in range: 
            # if i is in range, then update the value of current cell
            if (i == 0):
                continue
            if (i == 1): 
                nums[i] = max(nums[i], nums[i - 1])
            else: 
                nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
        # return the val of the last cell
        return nums[n - 1]
            
        

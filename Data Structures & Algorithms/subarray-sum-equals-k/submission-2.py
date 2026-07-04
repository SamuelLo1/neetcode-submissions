class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        return total num subarrays 
        sum equal k 

        [2, -1, 1, 2] k = 2
        iterate through array
        add to subarray if less than or equal to k 

        nums can be negative, k can get very large 

        O(N ^ 2) brute force: 
        double for loop 

        backtracking all subarray possibilities.
        diff

        issue: 
            - if I have negative values 
            - 2 - 0 --> -2
            - if I have a sum of -2 - 0 --> -2 
        """

        # record the prefixes: 
        prefixes = { 0 : 1 }

        # loop through array 
        curr_sum = 0
        res = 0 
        for i in range(len(nums)): 
            curr_sum += nums[i]
            # number to search for inside prefixes
            diff = curr_sum - k  
            if diff in prefixes: 
                # found a subarray for target
                res += prefixes[diff]

            # store the current prefix if not exists
            if curr_sum in prefixes: 
                prefixes[curr_sum] += 1
            else: 
                prefixes[curr_sum] = 1
        return res
            
                 
                



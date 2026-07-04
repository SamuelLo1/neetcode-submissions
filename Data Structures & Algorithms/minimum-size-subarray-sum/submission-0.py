class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        nums arr of pos ints
        pos int target
        return minimal length of subarray whose sum, grater than or equal target
        return 0 if no such

        Approach: 
        - create all possible subarrays. 
        - can either choose or not choose an element, don't need to pop 
        - for any path that is target or greater,
        - return the amount of elements it took to get to the path
        - return upwards the min amount 
        - if it has been calculated before return the memoized 
        - Time complexity: O(N * target)
        - target can get very large so this is not a good approach 

        Alternative approach
        - greedy approach? -- no 
        - can calculate the sums of all subarrays
        - and anytime a subarray equals to or is greater than target, 
        
        When trying to search for a specific subarray can do sliding window: 
        - 
        """

        l, total = 0, 0 
        res = float("inf")

        # Continue incrementing right pointer each time
        # Continuously remove elements until subarray is less than sum 
        # before adding next element
        for r in range(len(nums)):
            total += nums[r]
            while total >= target: 
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1
            
        return 0 if res == float('inf') else res




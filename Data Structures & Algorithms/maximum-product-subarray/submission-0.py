class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # doing brute force first is helpful to know what time complexity I am trying to beat

        """
        subarray: contiguous sequence of elements

        brute force: compute all the subarray's products 
            - O(N)^2
        thoughts: 
            - compute the current index, when I am onto next index look 
            - for maximum subarray of previous index 
            - negative numbers are present, greedy approach is difficult 
            - 
        """
        res = max(nums)
        curMin, curMax = 1, 1

        # for each number if 0, we want to reset the curMin and curMax
        # don't want to multiply nums by 0 
        for n in nums: 
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(n * tmp, n * curMin, n)
            
            res = max(res, curMax)

        return res 


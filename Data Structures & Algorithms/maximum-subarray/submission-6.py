class Solution:
    """
    find sub array with largest sum 
    return the sum 

    contain as little negative values as possible

    we only want to continue if the value we are adding won't 
    make our result negative
    else we take a new start. 

    we only need the value, so we can just maintain a maximum value to keep track 
    do an exhaustive search of the array

    sliding window approach: 

    Input: nums = [2,-3,4,-2,2,1,-1,4]
                        ^.          ^
    Output: 8


    constantly update if we find a better starting place
        - curr_sum 
        - next element

        if next element greater than curr_sum + next element
        we should start subarray at next element

        curr and next ptr can be on same el
        [2,3,-4,5]
         ^

        if it seems like a greedy type problem do multiple test cases, to be sure
        especially if there could be edge cases


    """
    def maxSubArray(self, nums: List[int]) -> int:

        if (len(nums) == 1): 
            return nums[0]

        ptr = 0
        curr_sum = 0
        max_sum = nums[0]

        while ptr < len(nums):
            
            #case 1: we want to reset sum and inc ptr (for greater value)
            if (curr_sum < 0):
                curr_sum = nums[ptr]
            #case 2: we want to add next element to subarray 
            else: 
                curr_sum += nums[ptr]
            ptr += 1
            max_sum = max(max_sum, curr_sum)

        return max_sum


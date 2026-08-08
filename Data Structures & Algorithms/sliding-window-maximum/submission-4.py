from collections import defaultdict
import heapq
class Solution:
    """
    Prob Notes: 
    - nums, k 
    return array with max element at each step

    Plan: 
    - keep track of curr max do an init window
    - loop until right < len
    - how do we get the max? 
        - process one el at a time, compare it with curr max 
        - update as go
        - keep count of curr max in a diff variable
        - how pop from heap
        - keep hashmap aswell -- tells me what elements are in the window, when they can be pooped from heap
        - use min heap

    process: 
        - peak top element, check if it is largest, if largest pop, else have while loop
        - if it still exists in hashmap can pop afterwards

    1211111
    - 2 

    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        result = []
        iter_max_el = -10000
        max_window_heap = []
        left = 0
        right = k - 1

        # intialize window and use min heap
        window = defaultdict(int)
        for i in range(k): 
            window[nums[i]] += 1
            heapq.heappush_max(max_window_heap, nums[i])
        
        window_iters = len(nums) - k 
        result.append(max_window_heap[0])

        # iterate the window 
        for j in range(window_iters): 
            # remove el
            # check if removed el is max and if so do heappops to get the current max after removing
            window[nums[left]] -= 1
            left += 1
            
            # get existing max after removing el 
            # check top of heap make sure it is in window remove els there
            while (max_window_heap and max_window_heap[0] in window and window[max_window_heap[0]] == 0): 
                heapq.heappop_max(max_window_heap)

            # compare existing max w/ new el
            right += 1
            window[nums[right]] += 1
            heapq.heappush_max(max_window_heap, nums[right])
            # update the result
            result.append(max_window_heap[0])            

        return result

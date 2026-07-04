class Solution:

    """
    slide through by keeping a hashmap of all the elements
    take out one and add one at a time
    can keep track of max and update as we add a new element or take out a new element
    
    when I remove an element, how do I know the new max
    can keep track of elements inside a heap going to pop if the top element is the one being removed

    - will need hashmap: 
        - tells frequency of each number within sliding 
        - add and subtract elements from window

    - will need heap: 
        - add elements into the heap when an element is removed.
            - when removing element from hashmap and freq = 0
            - pop from heap if max element is removed. 
            - continuously pop until an element exists in the hashmap
            - update windowMax to be between that element and new num being added
    
    - heap will be dirty but freq_map is constant updated

    # start with initialized window elements and heap and hashmap

    - dont think too optimally tried to think of O(N)    
    """
    import heapq
    from collections import defaultdict
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_array = []
        # initialize window with freq map and also initialize heap with elements
        freq_map = defaultdict(int)
        heap = [] # max heap needs to mult -1 
        window_max_el = nums[0]

        # return the next max element in the window
        def update_heap(heap, el_to_remove):
            while(heap): 
                new_max = -1 * heap[0] # peak the max element
                if (freq_map[new_max] > 0): 
                    return new_max
                else: 
                    heapq.heappop(heap)
            return -1 


        for i in range(k): 
            if (nums[i] in freq_map):
                freq_map[nums[i]] += 1
            else: 
                window_max_el = max(window_max_el, nums[i])
                freq_map[nums[i]] = 1
                heapq.heappush(heap, -1 * nums[i])

        max_array.append(window_max_el)

        # use for loop to loop through 1 , len(nums) - k + 1 
        # 4 + 3 - 1
        for i in range(1, len(nums) - k + 1): 
            # when removing i - 1 element update the max through popping a while loop
            remove_el = nums[i - 1]
            freq_map[remove_el] -= 1 
            print(freq_map, i)
            # need to remove whilst in freq map
            if (window_max_el == remove_el): 
                window_max_el = update_heap(heap, remove_el)
            # add an element i + k - 1, update global max, heap, and freq map, and append max to max array
            new_window_el = nums[i + k - 1]
            freq_map[new_window_el] += 1
            heapq.heappush(heap, -1 * new_window_el)
            window_max_el = max(window_max_el, new_window_el)
            max_array.append(window_max_el)
                
        return max_array

        
class Solution:
    """
    return the kth largest element in array
    maintain a heap

    nlog(k)

    [2,3,1,5,4], k = 2

    [2,3]
    peek the smallest element, if the current element is larger than the smallest, 
    pop the smallest and heappush the larger number. 
    
    maintain a size of 2. 
    after exhausting array: 
        pop from the heap one more time and that will be largest

    
    [2,3,1,5,4]
    [4,5]

    k = 1
    [1,1,1,1,1]

    
    out of k numbers, the smallest of the k yet, largest of the set
    maintains a kth largest factor
    """
    import heapq 
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        kth_largest = []
        heapq.heapify(kth_largest)
        


        for i in range(len(nums)):
            if len(kth_largest) >= k: 

                if (kth_largest[0] < nums[i]):
                    heapq.heappop(kth_largest)
                    heapq.heappush(kth_largest, nums[i])
                else: 
                    continue
            else: 
                heapq.heappush(kth_largest, nums[i])
        
        return heapq.heappop(kth_largest)
        
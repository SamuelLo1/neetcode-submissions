class Solution:
    """
    choose two heaviest stones: 
        - if x == y both destroyed
        - if x < y x is destroyed and y is y -x 
    continue until one stone remaining

    [2, 3, 6, 2, 4]

    [1]

    want to maintain a sorted ordering: 
        - each time we smash two stones insert back into a heap
        - can heapify array in O(N) time  

    heapify time complexity: 
        - essentially a flattened binary tree where the children are less than parents
            - In regular sorting each element is compared to at most log(n) other elements
            - In heapify only comparing 2 other elements at most 
    """
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        #neg for minheap to turn to maxheap
        for i in range (len(stones)): 
            stones[i] *= -1 
        
        heapq.heapify(stones)
        while len(stones) > 1: 
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            #print(abs(x), abs(y), abs(abs(x) -  abs(y)))
            heapq.heappush(stones, -1 * abs(abs(x) -  abs(y)))
            
        if (len(stones) == 0): 
            return 0
        else: 
            return abs(stones[0])

        
from heapq import heappush, heappop 
import math
class Solution:
    """
    return the k closest points to origin 0,0
    can calculate the euclidian distance of all the elements. 
    loop through array and insert into heap

    
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        max_heap = []

        for x, y in points:
            dist = -(x * x + y * y)  # use squared distance (no need for sqrt)
            heapq.heappush(max_heap, (dist, [x, y]))
            if len(max_heap) > k:
                heapq.heappop(max_heap)  # remove farthest

        return [point for (_, point) in max_heap]
            
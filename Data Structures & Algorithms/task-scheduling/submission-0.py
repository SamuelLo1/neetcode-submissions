from heapq import heappush, heappop, heapify
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        tasks completed in any order
        identical tasks need be seperated by n CPU cycles to cooldown the CPU 

        return minimum number CPU cycles to complete all tasks, 

        identical task cycles must be recomputed n times?

        - process most unique elements in one go, 
        - for remaining elements, process unique elements 
        - can have a freq map of letters
        - loop through letters --> i -- 26
        - can use ORD and chr
        """

        # create freq map
        freq_map = {}
        for i in range(len(tasks)): 
            if tasks[i] in freq_map: 
                freq_map[tasks[i]] += 1
            else: 
                freq_map[tasks[i]] = 1
        
        max_heap = [-cnt for cnt in freq_map.values()] 
        heapify(max_heap) # O(N) time

        time = 0
        q = deque() # store (-cnt, time)
        # while still tasks to be processed or max_heap still has elements to pop
        while max_heap or q: 
            time += 1

            if not max_heap: 
                time = q[0][1] # update time to whenever the first element can be released
            
            # pop the most frequent element 
            else: 
                cnt = heappop(max_heap) + 1
                # if cnt is not zero then append to q for idle time
                if (cnt): 
                    q.append((cnt, time + n)) # time + n is when the element can be freed
            
            if (q and q[0][1] == time): 
                cnt, time = q.popleft()
                heappush(max_heap, cnt)

        return time

        """
        A : 3 
        B : 1
        C : 1

        time = 1 
        max_heap = {-3,-1,-1}
        
        q = [(-2,2)]
    
        time = 2
        max_heap = {-1,-2}

        time = 3
        max_heap = {-1}
        q = [(-1,4)]



        """
            




            
        # want to add the most frequent elements into max heap

        # from max heap --> these are readily availible elements
        # can use a queue to keep track of elements that are on idle time, 
        # tasks that cannot be repeated again
        # don't actually need to store keys in maxheap
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        directed edges
        nodes labeled 1 - n 
        times weighted edges with time

        integer k is node to send signal 
        return minimum time for all n nodes to recieve signal from k: 
        return -1 if not possible for all other nodes to recieve signal
        djikstras algo: 

        by using djikstras, since can get to every node, the node w/ greatest
        work through examples, and really understand the problem, I could be solving for the wrong thing

        here, I blindly assumed that I was solving for total time 
        but network travels in parallel so I just needed the maximum amount of time from djikstras
        and to ensure that every node can be discovered.

        If I was to get minium path to traverse all nodes, can do a bfs traversal of entire
        heapq is only used for when array has more than one elements 

        if dense graph: 
            E can turn into V^2 
            this means that the time complexity for E * log(V) can turn into V^2 log(V)
            so the default way of finding the min from the queue is better because we can 
            go through in O(V^2) time

        heap notes: 
            - python's heap is min heap by default 
            - heapify only needed for unsorted arrays 
            - for tuples passed in, heapq compares first element, then second element, so on... 
        """

        # create adj list: directed
        edges = collections.defaultdict(list)
        for u,v,w in times: 
            edges[u].append((v,w))

        # initialize heap: weight, node 
        minheap = [(0,k)]
        visit = set() 
        t = 0

        # continue going through heap
        while minheap: 
            w1, n1 = heapq.heappop(minheap)
            if n1 in visit: 
                continue
            visit.add(n1)
            t = w1 
            
            # go through neighbors and explore what to add next
            # add each neighbor to minHeap and let the heap figure out which edge to process next 
            for n2, w2 in edges[n1]: 
                if n2 not in visit: 
                    heapq.heappush(minheap, (w1+w2, n2))
            
        return t if len(visit) == n else -1 
        


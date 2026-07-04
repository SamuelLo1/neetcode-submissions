class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        given sorted int array, 
        two ints k and x
        return k closest elements to x 

        sorted in ascending order

        if |a - x| == |b - x| then if a is less than b choose a first
        can binary search for location where x would be

        how can I binary search for the element 
        """

        l = 0
        r = len(arr) - 1

        # binary search for element 
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < x: 
                l = mid + 1
            else: 
                 r = mid 
        
        # now that we have pointers initialized
        l,r = l - 1, l
        print(l,r)
        # do two pointers that grow window around kth element 
        k_found = 0
        while k_found < k: 
            k_found += 1
            # bounds check to know which side to increment
            if l < 0: 
                r += 1
                continue
            elif r > len(arr) - 1: 
                l -= 1
                continue

            left_diff = abs(arr[l] - x)
            right_diff = abs(arr[r] - x) 
            # left less
            if (left_diff <= right_diff):
                l -= 1
            else: 
                r += 1
        return arr[l + 1:r]
            
        





    
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        given a string s only uppercase
        choose k chars
        replace with any uppercase char
        after k replacements 
        return length of longest substr with only one distinct char

        "sliding window with k size": 
        
        through iterations can keep track of first mismatch
        start traversal after first mismatch

        can I use a set for this? 
        looping through each element and storing it in a set
            - X
        AABABAA

        optimal: 
        sliding window: 
        keep a sliding window and keep track of an element that I remove and decrement hashmap 
        ensure that the values that are not the max are always equal to k 
        """

        count = {}
        res = 0
        l = 0 
        maxf = 0 
        #collect element in the frequency list 
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]]) 

            #this is a condition that triggers only when window does not support transforming k elements
            #shrink the window to ensure that the requirement that k elements replaced retains
            #by shrinking window size, we will get a value that is equal k 
            if ((r - l + 1) - maxf > k): 
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
            
            


        #instead of counting the elements can use window size to keep track
        #only need the maximum element subtract from window size
        #dynamic window size, can be maximum element add on k   

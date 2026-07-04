class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        given two strings s1 s2
        true s2 contains permutation of s1
    
        - a permutation of s1 exists as a substring within s2
        - letters can be ordered however characters must all be present
        
        "we know s1 is of length 3" 
         can check 3 chars at a time
        s1 = "abc" 
        s2 = "lecabee"

         both hashmaps can be initialized 26 english alpha

         can also keep a hashmap to ensure we have same characters as s1
         create a hashmap of s1 


         maintain a sliding window for s2 of size len(s1)
         increment: add new el to curr hashmap
         decrement: remove el from curr hashmap

         {
            l : 
            e : 1
            c : 1
         }
        """
        if len(s1) > len(s2): 
            return False
            
        #create hashmap for first
        s1_chars = {} 
        windows_chars = {}

        #initialize hashmaps
        for i in range(26): 
            s1_chars[chr(97 + i)] = 0 
            windows_chars[chr(97 + i)] = 0 
        
        #populate hashmap
        for char in s1: 
            s1_chars[char] += 1
        

        #sliding window 
        left = 0 
        right = len(s1)
        

        for i in range(right): 
            windows_chars[s2[i]] += 1 

        while (left < len(s2) and right < len(s2)): 
            if (windows_chars == s1_chars): 
                return True
            windows_chars[s2[right]] += 1
            windows_chars[s2[left]] -= 1
            right += 1
            left += 1
        return windows_chars == s1_chars    

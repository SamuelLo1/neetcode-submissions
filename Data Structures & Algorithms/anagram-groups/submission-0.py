from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        given array strs, group all anagrams into sublists
        What is an anagram:    
            - contains same characters of another string but same order
        can be returned in any order

        constraints: 
        strs.length <= 1000
        strs[i].length <= 100 
        all lowercase english letters

        Input: strs = ["act","pots","tops","cat","stop","hat"]
        Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

        Questions: ask for constraints
        - ask for order if not mentioned

        approach
        for each element, check with other elements 
        make a frqList of this element 
        if their frqList is equal to this hashmap,
        append to an array, 

        else: 
        
        """

        def createFreqList(s): 
            alphabet = []
            freq = [0]*26
            for i in range(26): 
                alphabet.append(chr(i+97))
            alpha_tuple = tuple(alphabet)
            
            for i in range (len(s)): 
                index = ord(s[i]) - 97
                freq[index] += 1
            
            return tuple(zip(alpha_tuple, freq))

        groups = defaultdict(list)
        result = []

        for i in range(len(strs)): 
            current_freq = createFreqList(strs[i])
            if (current_freq in groups): 
                groups[current_freq].append(strs[i])
            else: 
                groups[current_freq] = [strs[i]]
        
        for key,value in groups.items(): 
            result.append(value)
            
        return result
        
        
        
        

            
        
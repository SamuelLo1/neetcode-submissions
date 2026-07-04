class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Thinking: 
            - can keep a freq count 
            - how will we know chars that still needed 
            - s = "OUZODYXAZV", t = "XYZ"
            - can keep a window size of the size of t
            - as soon as find char move window 
            - check the frequencies if they appear in the window if not continue 
            - incrementing: 
            - O(N * t)
        """
        # initialize freq counts and variables
        window_count, target_count = {}, {}
        characters_fufilled = 0 # keep track of how many characters still looking for in window
        res_len = float("infinity")
        res_range = [-1,-1]

        # populate freq counts
        for c in t: 
            # fast way to update target_counts
            target_count[c] = 1 + target_count.get(c, 0)
            window_count[c] = 0
        
        # traverse string with sliding window 
        # while I have a solution ( freqs match, narrow in left boundary )
        # update the resLen each time I update the left boundary
        l = 0
        for r in range(len(s)): 
            # add the current character to the freq counts
            if s[r] in window_count: 
                window_count[s[r]] += 1 
                if (window_count[s[r]] == target_count[s[r]]):
                    characters_fufilled += 1
            
            while characters_fufilled == len(target_count):
            # if the removed character is a crucial character 
            # update the freq map 
            # update variables
                if (r - l + 1) < res_len: 
                    res_len = r - l + 1
                    res_range = [l,r + 1]
                if s[l] in window_count:
                    window_count[s[l]] -= 1
                    if (window_count[s[l]] < target_count[s[l]]):
                        characters_fufilled -= 1
                l += 1
        
        if res_len == float('infinity'): 
            return ""
        else: 
            return s[res_range[0]:res_range[1]]
                    
                    



        
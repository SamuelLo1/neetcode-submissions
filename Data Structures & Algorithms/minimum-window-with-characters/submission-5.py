from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        every char in t is present in S. 
        correct output is unique
        shortest substring : string portion

        brute force: 
        - have window size t
        - have hashmap (update it)
        - check for 

        - get window for all chars of t inside
        - remove one char at a time
        - if removing still forms t, continue updating min count and min substring
        OUZODYXAZV
        XYZ
        """
        
        min_substr = ""
        min_count = float('inf')

        # loop until we match every char of t with every char of substring
        left = 0
        right = 0
        s_freq_dict = defaultdict(int)
        t_freq_dict = defaultdict(int)

        # populate t_freq
        for letter in t: 
            t_freq_dict[letter] += 1

        # track how many unique characters in t have their requirements met
        required = len(t_freq_dict)
        formed = 0

        # loop through and continue incrementing right until the end
        while right < len(s): 
            # increment right and add to dict
            char = s[right]
            s_freq_dict[char] += 1
            
            if char in t_freq_dict and s_freq_dict[char] == t_freq_dict[char]:
                formed += 1
            
            right += 1
            # check if match with t, update mins
            # remove first char 
            while formed == required: 
                # update mins
                if (min_count > right - left):
                    min_count = right - left
                    min_substr = s[left:right]
                
                # remove first char, inc left
                removed_char = s[left]
                if removed_char in t_freq_dict and s_freq_dict[removed_char] == t_freq_dict[removed_char]:
                    formed -= 1
                
                s_freq_dict[removed_char] -= 1
                left += 1

        return min_substr
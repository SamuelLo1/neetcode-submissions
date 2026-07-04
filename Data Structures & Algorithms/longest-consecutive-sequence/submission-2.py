class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Algorithm that runs O(n)
        consecutive: sequence of els each greater than prev by 1 

        return longest consecutive sequence
        elements can be ordered however

        hashmap for O(1)
        store each element in map, 

        for each element we can go through and check if next is in hashmap. Use a while loop and increment 
        can keep track of visited to know which ones I have already discovered

        key idea: 
            - if I previously walked through an element in visited from another el, the current element is not the 
            largest and does not need to be rediscovered. 
            - duplicates: duplicates don't matter because they would get ignored

        [0,3,2,5,4,6,1,1]
        {0, 3, 2, 5, 4, 6, 1}
        for each element keep track of a largest seq 
        check if the element is in visited
        visited: {0, 1, 2, 3, 4, 5, 6}

        Time complexity: 
            - create set: O(N)
            - go through and find largest subsequence: O(N)
        Space complexity:
            - O(N)
        """

        if not nums: 
            return 0 

        visited = set() #avoids dups
        sequenced = set()
        for i in range(len(nums)): 
            sequenced.add(nums[i])
        
        largest_sequence_len = 1
        for i in range(len(nums)): 
            curr_num = nums[i]
            curr_sequence = 1
            if curr_num in visited: 
                continue
            visited.add(curr_num)
            
            while (curr_num + 1 in sequenced):
                visited.add(curr_num + 1)
                curr_num += 1 
                curr_sequence += 1
                if (curr_sequence > largest_sequence_len): 
                    largest_sequence_len = curr_sequence
        
        return largest_sequence_len 

        



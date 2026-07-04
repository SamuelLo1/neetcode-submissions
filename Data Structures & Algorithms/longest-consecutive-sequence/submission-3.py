class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        return length of longest consec sequence elements

        O(n) time

        how keep track of longest? 
        can sort the array nlogn

        questions? 
        - do negative numbers count

        can have a hashmap: 
        
        store each number: can check if the +1 or -1 of this element exists, if it does update the dictionary
        use the stored value
            - only update if does not already exist
            - if both +1 and -1 exist, then increment 2
            - if I find a 1 later on how do update 2


        # left border = current 
        # right border = current 
        # think about it, we will only be adding numbers to the borders, won't be adding numbers to the middle
        # try to strip away as much info as not needed
        2,3,4,5,6
        {
            2 : [2]
            20 : [20]
            4: [4]
        }
        """
        num_map = defaultdict(int)
        res = 0 

        for num in nums: 
            # is it true that if border then everything in between is good
            if (num_map[num] == 0): 
                # joining two consecutive sequences
                num_map[num] = num_map[num - 1] + num_map[num + 1] + 1
                # update the borders
                num_map[num - num_map[num - 1]] = num_map[num]
                num_map[num + num_map[num + 1]] = num_map[num]
                res = max(res, num_map[num])

        return res


        



        



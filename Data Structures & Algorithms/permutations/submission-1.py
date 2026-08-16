class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        """
        return all possible permutations
        [1,2,3]
        []
      1, 2, 3
    1, 2, 3  

        """ 

        # backtrack through elements
        def backtrack(flipped, curr): 
            # check if curr length 
            if (len(curr) == len(nums)): 

                self.result.append(curr[:])
                return 

            # loop through each num in nums
            for j in range(len(nums)): 
                # previous backtracking step already added this el to curr
                if (flipped[j]): 
                    continue
                flipped[j] = True
                curr.append(nums[j])
                backtrack(flipped, curr) 
                flipped[j] = False    
                curr.pop()


        self.result = []
        flipped = [False] * len(nums)
        backtrack(flipped, [])

        return self.result

        #



class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #check while less than target, explore tree possibilities
        
        #question: 
            #are negatives allowed 
        #match:
            #return a set of arrays? 
            #array for result return
            #visited set for each number that is approached? 
            #can use a hashing method on the array to show a num is visited



        #plan: 


        """
        - return a list of all unique combinations of candidates that sum to target
        - each element chosen at most once 
        """

        targetSums = []
        currNums = []
        nums = sorted(candidates)
        def backTrack(index):
            
            #conditions for appending to targetSums 
            if (sum(currNums) == target): 
                targetSums.append(currNums[:])
                return
            elif(sum(currNums) > target): 
                return

            #oor
            if (index == len(nums)): 
                return 

            for i in range(index, len(nums)): 
                # do not repeat tries that have same number
                if (i != index and nums[i - 1] == nums[i]): 
                    continue
                currNums.append(nums[i])
                backTrack(i + 1)
                currNums.pop()

        backTrack(0)

        return targetSums
            


        
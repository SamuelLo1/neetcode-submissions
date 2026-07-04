class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsets = []
        currentNums = []
        subsets.append([])

        def dfs(i): 
            
            #if past the last index, then add to result
            if (i == n):
                return 
            
            #array takes current number
            currentNums.append(nums[i])
            subsets.append(currentNums[:])
            dfs(i + 1)
            currentNums.pop()
            dfs(i + 1)

        dfs(0)
        return subsets
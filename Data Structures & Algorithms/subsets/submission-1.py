class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:


        n = len(nums)
        subsets = []
        current = []
        #start with empty array
        subsets.append([])

        #
        def dfs(i): 
            #basecase return at this depth of tree
            if (i == n): 
                return

            current.append(nums[i])
            dfs(i + 1)
            subsets.append(current[:])
            current.pop()
            print(current)
            dfs(i + 1)

        dfs(0)
        return subsets
            
            
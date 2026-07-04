class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        perms = []
        currNums = []
        used = [False for _ in range(len(nums))]
        nums.sort()  # Sort to group duplicates together

        def dfs():
            if len(currNums) == len(nums):
                perms.append(currNums[:])
                return

            for i in range(len(nums)):
                # Skip used elements or duplicates at the same level
                if used[i] :
                    continue
                
                used[i] = True
                currNums.append(nums[i])
                print(currNums)
                dfs()
                currNums.pop()
                print(currNums)
                used[i] = False

        dfs()
        return perms
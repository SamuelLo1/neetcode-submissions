class Solution:

    """
        - return list of all unique combos of nums that sum to target
        - each num can be used unlimited
        - any order
        - backtracking: 
            - add all numbers first and if too high, 
    """
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(i , cur, total): 
            #basecase for when target is hit, return res.copy
            if total == target: 
                res.append(cur.copy())
                return

            #out of bounds
            if i >= len(nums) or total > target: 
                return 

            #traverse 
            cur.append(nums[i])

            #continue to add current number until it becomes too big, will return and can pop
            dfs(i, cur, total + nums[i])
            cur.pop()
            #go to next number to check if within bounds, if out of bounds, it will keep going until all is return
            #since we check for total out of bounds and i out of bounds, the i will eventually return
            dfs(i + 1, cur, total)
        dfs(0,[],0)
        return res


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        return integer that appears more than once
        
        cycle in linked list insinuates that there is a duplicate, 
        this only works because linked list is n + 1 size and only 
        has range of [1,n], meaning there must be duplicate
        """
        # -- hare and tortoise (gaurenteed cycle) -- 
        slow, fast = 0, 0
        while (True): 
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: 
                break

        # -- want to look for the cycle node --
        # start slow node at start and slow node at the point where it was broken,
        # find where they meet  

        slow_start = 0
        while (True): 
            slow = nums[slow]
            slow_start = nums[slow_start]
            if slow == slow_start: 
                return slow 




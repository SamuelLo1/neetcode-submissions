# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        cycle if one node in list visited again via next ptr
        index: determines index of beg of cycle
        if index = 01, the tailnode points to -1 and no cycle exists

        thinking:
         can keep a ptr at the index, have another ptr iterate through
        if the iterating ptr ever is equal to the ptr at the index, then return cycle
        else: if the iterating ptr finds -1 then return false

        note: index is not param
        so anchor point is tailnode, if it is explored twice, then return false
        """

        visited = set()
        curr = head
        while(curr is not None): 
            #traversed node before
            if(curr in visited): 
                return True
            
            visited.add(curr)  
            curr = curr.next
            
        return False



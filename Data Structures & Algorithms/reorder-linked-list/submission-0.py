# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """

        can easier manipulate with external data structure: array
        and reorder with that


        """

        #create array
        hashSet = set()
        order = []
        links = []
        curr = head
        while curr is not None: 
            hashSet.add(curr)
            links.append(curr)
            curr = curr.next
        
        #re-order array
        l = 0 
        r = len(links) - 1
        count = 0 
        while (l <= r): 
            if(count % 2 == 0): 
                order.append(links[l])
                l += 1
            else: 
                order.append(links[r])
                r -= 1
            count += 1

        curr = head
        for i in range(1,len(order)): 
            curr.next = order[i]
            curr = curr.next
        
        curr.next = None
        

        

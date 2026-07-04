# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
turn linked list into list and 
and then edit the linked list  = 

"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #set the head node

        dummy = ListNode()
        dummy.next = head

        slow = dummy
        fast = head
        #iterate to the nth node with slow pointer
        for i in range(n): 
            fast = fast.next
        
        #iterate to the end of list and remove slow pointer's value
        while fast: 
            slow = slow.next
            fast = fast.next
        
        if(slow.next.next): 
            slow.next = slow.next.next
        else: 
            slow.next = None

        return dummy.next
        

    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        singly linked list
        reverse linked list from left to right 

        reverse only a portion of the linked list 

        left and right are integers
        can keep track of left and right here 
        
        can I use extra memory and just reverse the linked list 
        by storing the elements 

        can stake pointers at left and right

        1 2 3 4 5
        o   x n

        update n each time 

        can increment o ptr until reaches node pointed by x ptr
        1 2 3 4 5
          x.    o 
        
        1 3 4 5 2


        1 2 3 4 5 6 
            o
        1 2 4 3 5 6 

        better strategy to avoid making dummy node at end is to have dummy node in front 
        of list and move elements to front of list 
        """

        # increment pointers to left and right positions first 
        dummy = ListNode(0)
        dummy.next = head 

        # get left and right nodes
        prev = dummy
        for i in range(left - 1): 
            prev = prev.next 

        left_head = prev.next 
        right_tail = left_head
        for i in range (right - left): 
            right_tail = right_tail.next
        print("These are the head and tail values:", left_head.val, right_tail.val)

        next_node = right_tail.next 
        right_tail.next = None # remove tail so that can reverse the list
        reversed_list = self.reverseList(left_head)
        prev.next = reversed_list
        left_head.next = next_node 
        return dummy.next

    def reverseList(self, head): 
        prev, curr = None, head 

        while curr: 
            temp = curr.next
            curr.next = prev
            prev = curr 
            curr = temp

        return prev 






            
        





        
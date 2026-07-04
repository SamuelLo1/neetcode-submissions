# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Notes: 
        - k linked lists
        - sorted ascending 

        return sorted order of linked lists

        Brute force: 
        - for each of the k lists, have a pointer to their leftmost node
        - can use a dummy in each linked list: 
        - use a smallest to track smallest of the k list pointers
        - after traversing, add the smallest, and remove from left side one of nodes
        - continue until all the lists are None: 
        - how can I know if a list is empty? its pointer is None
        """

        # add a dummy node for each linked list: 
        # don't need to delete nodes can just traverse to next node 
        k = len(lists)
        dummy_node = ListNode(-1)
        curr_building_node = dummy_node

        while True: 

            traversed_lists = 0
            smallest_curr = float('inf')
            list_taken_from = -1 
            # loop through each list and compare elements to add to final array
            for i in range(k): 
                curr = lists[i]
                if (not curr): 
                    traversed_lists += 1
                    continue
                if (curr.val <= smallest_curr): 
                    list_taken_from = i
                    smallest_curr = curr.val
            
            if traversed_lists == k:
                break 

            # update the taken from list 
            node_to_update = lists[list_taken_from]
            lists[list_taken_from] = node_to_update.next 
        
            # build our linked_list
            curr_building_node.next = node_to_update 
            curr_building_node = curr_building_node.next
            
        
        return dummy_node.next




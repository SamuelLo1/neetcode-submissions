"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        use an array to keep track of the linked list, 

        first pass: populate list with the original nodes
        second pass: can populate the random field of the nodes 
        """

        #how to get the index of a random
        #hashmap node_val -> index in list
        #hashmaps past python 3.7 maintain insert order
        node_index_mappings = {}
        random_node_indexes = []

        deep_copy = []
        curr = head

        i = 0 
        while curr: 
            #create new listNodes for deep_copy
            deep_copy_node = Node(curr.val, None , None)
            deep_copy.append(deep_copy_node)

            node_index_mappings[curr] = i
            i += 1
            curr = curr.next
        print(node_index_mappings)
        #ith node in order of insertion's random index 
        j = 0 
        for key,index in node_index_mappings.items(): 
            if (key.random): 
                randomIndex = node_index_mappings[key.random]
                deep_copy[j].random = deep_copy[randomIndex]
            #set the next pointer
            if (j + 1 < len(deep_copy)):
                deep_copy[j].next = deep_copy[j + 1]
            j += 1

        if len(deep_copy) > 0: 
            return deep_copy[0]
        else: 
            return None


class ListNode: 
    def __init__(self, value): 
        self.value = value 
        self.next = None

class MyCircularQueue:
    """
    Queue
    - last pos connected to first pos
    "Ring Buffer" 

    Notes: 
    - cannot use built in queue 
    
    Full happens when all the positions are filled 
    O(N)

    would walk through to see if the queue is empty, 

    why would an array be bad? 
    - 
    [1,2,3]
    3 O(1)
    is full : O(N)
    deque: O(N)
    - would need to keep track of the 

    linked list: 
    - if linkedlist is empty, head is None. 
    - to enqueue, should find where it is empty to enque 
    - keep track of tail ptr
    - to remove something use the tail ptr and one ptr ahead of the actual head ptr

    head and tail reference the same place in memory, one pointer can change,
    the other will still reference the same object
    """

    # intialize circular queue with size k 
    def __init__(self, k: int):
        self.head = None
        self.tail = None
        # create empty linked list Values set to -1 
        self.linked_list = self.create_linked_list(k)

        # check linked list created
    def create_linked_list(self, k: int):
        self.head = ListNode(-1)

        curr = self.head
        for i in range (k - 1): 
            new_node = ListNode(-1)
            curr.next = new_node
            curr = curr.next 
        
        # create cycle 
        self.tail = curr
        self.tail.next = self.head

        return self.head

    # insert, return true if successful
    # if value of head is -1 update the value
    # update tail ptr 
    def enQueue(self, value: int) -> bool:
        # ensure list is not full
        if self.tail.next.value != -1: 
            return False
        else: 
            # enqueue value and update tail 
            self.tail.next.value = value 
            self.tail = self.tail.next 
            return True

    # deletes head element, make head -1. 
    # update head to the next link in the linked list
    def deQueue(self) -> bool:
        if self.head.value == -1: 
            return False    
        else: 
            self.head.value = -1 
            self.head = self.head.next 
            return True

    # get front item from queu, return -1 if empty
    def Front(self) -> int:
        return self.head.value

    # get the last item from queue, return -1 if empty
    def Rear(self) -> int:
        return self.tail.value

    # O(1) if tail is empty 
    def isEmpty(self) -> bool:
        if (self.head.value == -1): 
            return True
        else: 
            return False

    def isFull(self) -> bool:
        if (self.head.value != -1 and self.tail.next.value != -1): 
            return True
        else: 
            return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
class StockSpanner:

    def __init__(self):
        self.span_stack = []

    def next(self, price: int) -> int:
        # if stack empty append regardless
        if len(self.span_stack) == 0: 
            self.span_stack.append((price, 1)) # add price span
            return 1
        # if element less than prev element append
        if (self.span_stack[len(self.span_stack) - 1][0] > price): 
            self.span_stack.append((price, 1))
            return 1 

        # if element greater than prev element, start popping and adding to sum 
        # make sure to add this new element to stack
        curr_span = 1
        while (self.span_stack and self.span_stack[len(self.span_stack) - 1][0] <= price): 
            stock_price, stock_span = self.span_stack.pop() 
            curr_span += stock_span
        
        self.span_stack.append((price, curr_span))
        return curr_span 
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

"""
collect daily price quotes
stock's price is max consec 

stock can span any previous days where it is less than or equal curr value
- the values can be random, 
- partitions aren't definite increasing/decreasing
- can maintain a sequence of numbers less than current at any point
- memoization? only need to know about most recent span
- maintining current streak value
- 

curr span 70 : 2
curr span 60 : 1
if can collect most recent element, it continues to collect down the stack 
[]

{ 100, 80, 60, 70, 60 }
"""
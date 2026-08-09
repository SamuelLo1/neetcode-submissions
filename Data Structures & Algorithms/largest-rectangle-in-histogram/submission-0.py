class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        return area of largest rectangle

        - insert onto stack only if larger
        - intuition is that everything to the right of the element follows a staircase and we can take the index of a previous up to curr and establish a max area and pop 
        - now need to update newly inserted smaller el to be at the position we last popped at
        """
        largest_rect = heights[0]
        mono_stack = [(0,heights[0])]
        # loop through and insert into stack if larger
        for i in range(1,len(heights)): 
            rect_size = 0
            min_index = i
            # add to mono stack if larger
            # if less than loop through and pop and update largest rect
            while (mono_stack and heights[i] < mono_stack[-1][1]): 
                pop_ind, pop_height = mono_stack.pop()
                min_index = pop_ind
                width = i - pop_ind
                largest_rect = max(largest_rect, width * pop_height)

            if (not mono_stack or mono_stack[-1][1] != heights[i]): 
                mono_stack.append((min_index, heights[i]))
            
            # if equal do nothing, update largest rect
        
        while mono_stack: 
            pop_ind, pop_height = mono_stack.pop()
            width = len(heights) - pop_ind

            largest_rect = max(largest_rect, width * pop_height)
        
        return largest_rect



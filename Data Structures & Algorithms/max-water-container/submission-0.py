class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        start two pointers on either side of the array  

        two factors for max area: 
            - distance apart, 
            - the minimum between left and right heights
        
        to check if worth moving up: 
            - min * distance 

            - take into acc: larger * distance - 1: would it be worth 
            looking for a better one? 
            - keep track of a max. 
            - always want to decrement the smaller one until the two pointers cross
        """
        max_area = 0 
        left = 0 
        right = len(heights) - 1

        while left < right: 
            curr_height = min(heights[left], heights[right])
            max_area = max(max_area, curr_height * (right - left))

            if heights[left] < heights[right]: 
                left += 1
            else: 
                right -= 1

        return max_area

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        """
        COMMENT
        """

        res = [0] * len(temperatures)
        stack = []

        #go through each temperature
        for i, t in enumerate(temperatures):
            #if we find a bigger element, populate smaller elements in the stack
            while stack and t > stack[-1][0]: 
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))

        return res


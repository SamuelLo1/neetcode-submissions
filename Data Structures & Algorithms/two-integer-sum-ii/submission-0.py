class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        array is sorted
        index1 cannot equal index2

        exactly one valid solution only 

        Questions: 
        - are elements unique
        - What are the constraints as in max number we can take in
        - Can negative numbers be allowed

        Psuedo: 
        
        1-indexed, so just add 1 to everything

        first 
        second
        ptr on either side : can either make our curr sum smaller or greater 
        if greater, decrement second ptr
        if lesser, increment first ptr 
        if equal, return both ptr's numbers
        1 2 



        go through until both dont touch

        """
        first = 0
        last = len(numbers) - 1

        while first < last: 
            curr_sum = numbers[first] + numbers[last]
            if (curr_sum == target): 
                return [first + 1, last + 1]
            elif (curr_sum < target):
                first += 1
            else: 
                last -= 1
 


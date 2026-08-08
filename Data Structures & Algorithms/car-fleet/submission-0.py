class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        pos and speed array

        car catches up to car ahead and goes same speed

        - how can we determine if cars merge into fleet?
        - (target - position) / speed = time 
        - if time to get to dest is equal or less than then a fleet is formed
        - sorting makes sense with tuples
        - do I go in reverse - yes

        Things: 
            - the fleets are bounded by the minimal speed of a car ahead, position matters
            - sorting is the key here 
        """
        stack = []
        sorted_cars = []
        # form tuple list and sort by distances 
        for i in range(len(position)): 
            sorted_cars.append((position[i], speed[i]))

        sorted_cars.sort(reverse=True)
        # loop in reverse
        for car_pos, car_speed in sorted_cars: 
            time_to_finish = (target - car_pos) / car_speed
            
            # if less than stack top, don't add if more than stack top add
            if stack and time_to_finish <= stack[-1]:
                continue
            else: 
                stack.append(time_to_finish)
        

        # calculate the time to get to target, compare if less than join same fleet: 
        # if more than, form new fleet: 


        return len(stack)

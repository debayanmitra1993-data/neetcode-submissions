class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [None]*len(position)
        for idx in range(len(position)):
            cars[idx] = (position[idx], speed[idx])
        cars.sort(key = lambda x : x[0])

        mystack = [cars[-1]]

        for idx in range(len(cars) -2, -1, -1):
            car = cars[idx]
            # check if this car can catchup to the car ahead before reaching the destination...
            car_speed = car[1]
            car_pos = car[0]

            t_car_dest = (target - car_pos)/car_speed

            t_car_prev_stack = (target - mystack[-1][0])/mystack[-1][1]
            
            if t_car_dest <= t_car_prev_stack:
                pass
            else:
                mystack.append(car)
        return len(mystack)  


        
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        outstack = []

        while len(asteroids) > 0:

            # check if outstack is empty...
            if len(outstack) == 0:
                popped = asteroids.pop()
                outstack.append(popped)
            
            if len(asteroids) == 0:
                break

            # check if collision will happen....
            if asteroids[-1] > 0 and outstack[-1] < 0:
                pop_asteroid = asteroids.pop()
                pop_outstack = outstack.pop()
                if abs(pop_asteroid) == abs(pop_outstack):
                    result = None
                elif abs(pop_asteroid) > abs(pop_outstack):
                    result = pop_asteroid
                elif abs(pop_asteroid) < abs(pop_outstack):
                    result = pop_outstack
                
                if result is not None:
                    asteroids.append(result)
            else:
                popped = asteroids.pop()
                outstack.append(popped)
        
        finaloutstack = []
        while len(outstack) > 0:
            ele = outstack.pop()
            finaloutstack.append(ele)
        return finaloutstack
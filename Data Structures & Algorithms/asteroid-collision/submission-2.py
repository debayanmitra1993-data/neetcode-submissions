class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ele = asteroids.pop()
        tempstack = []
        tempstack.append(ele)

        while len(asteroids) > 0:
            if len(tempstack) == 0:
                ele = asteroids.pop()
                tempstack.append(ele)
            
            if tempstack[-1] < 0 and asteroids[-1] > 0:
                if abs(tempstack[-1]) == abs(asteroids[-1]):
                    tempstack.pop()
                    asteroids.pop()
                elif abs(tempstack[-1]) > abs(asteroids[-1]):
                    asteroids.pop()
                elif abs(tempstack[-1]) < abs(asteroids[-1]):
                    tempstack.pop()
            else:
                if len(asteroids) > 0:
                    ele = asteroids.pop()
                    tempstack.append(ele)
                else:
                    break
        
        

        
        print("asteroids = ", asteroids)
        print("tempstack = ", tempstack)
        while len(tempstack) > 0:
            ele = tempstack.pop()
            asteroids.append(ele)
        return asteroids

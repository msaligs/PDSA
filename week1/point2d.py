class Point:
    def __init__(self,x,y):
        '''
            intialise a 2D point using x and y coordinate
        '''
        self.x = x
        self.y = y
    
    def translate(self,deltax,deltay):
        '''
            translate the point by x unit horizontaly and y unit vertically
        '''
        self.x += deltax
        self.y += deltay

    def odistance(self):
        '''
            distance from origin
        '''
        import math
        d = math.sqrt((self.x**2)+(self.y**2))
        return d
    
    def __add__(self,p):
        '''
            add 2 points
        '''
        # self.x = self.x + p.x
        # self.y = self.y + p.y
        return Point(self.x + p.x,self.y + p.y)
    
    def __str__(self):
        return (
            '(' + str(self.x) + ','+ str(self.y) + ')'
        )

import math
class Point1:
    def __init__(self,x,y):
        self.r = math.sqrt(x**2 + y**2)
        if x == 0:
            self.theta = math.pi/2
        else:
            math.atan(y/x)

    def odistance(self):
        return self.r
    
    def translate(self,deltax,deltay):
        x = self.r * math.cos(self.theta)
        y = self.r * math.sin(self.theta)

        x = x + deltax
        y = y + deltay

        self.r = math.sqrt(x**2 + y**2)
        if x == 0:
            self.theta = math.pi/2
        else:
            self.theta = math.atan(y/x)

    

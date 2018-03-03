from math import pi
class Shape(object):
    def __init__(self):
        raise NotImplementedError

    def area(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self,x,y,r):
        self.center=(x,y)
        self.radius=r

    def area(self):
        return pi*(self.radius**2)

    def __str__(self):
        return '"Circle at {0} radius {1}"'.format(self.center,self.radius)

class Polygon:
    def __init__(self,vertex):
        self.vertex=vertex

    def area(self):
        sum=0
        self.x=[]
        self.y=[]
        no_of_corner=len(self.vertex)

        for i in range(0,no_of_corner-2):
            if i==0:
                j=no_of_corner-1                            #x0=Xn  and y0=yn
            else:
                j=i
        sum+=(self.vertex[j][0]*self.y[i+1][1])-(self.x[i+1][0]*self.y[j][1])
        return sum/2;                                           #area= 1/2(sum)

    def __str__(self):
        return '"Polygon with {0}"'.format(self.vertex)

c=Circle(1,3,2)
print(c)
print(c.area())

p=Polygon([(1,2),(3,4),(5,6),(4,8)])
print(p)
print(p.area())

print(len(p.vertex))

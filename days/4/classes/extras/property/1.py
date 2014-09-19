import math

class Circle:
    def __init__(self, r):
        self.radius = r
    
    @property
    def area(self):
        return math.pi*(self.radius ** 2)


c = Circle(1)
print 'radius = %d' % c.radius
print 'area = %f' % c.area




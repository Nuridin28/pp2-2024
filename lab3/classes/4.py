import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x,self.y)
    def move(self, x_ch, y_ch):
        self.x = x_ch
        self.y = y_ch
    def dist(self):
        print(abs(x-y))

p1 = Point(1, 4)
p1.show()
p1.move(1, -2)
p1.show()
p1.dist()
        

    

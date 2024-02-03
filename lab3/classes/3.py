class Shape:
    def __init__(self,leng):
        self.leng = leng
    def area(self):
        a = self.leng*self.leng
        print(a)

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def area(self):
        print(self.l*self.w)

x = Rectangle(4, 5)
x.area()
    


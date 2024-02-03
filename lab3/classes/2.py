class Shape:
    def __init__(self,leng):
        self.leng = leng
    def area(self):
        a = self.leng*self.leng
        print((a))

class Square(Shape):
    def __init__(self, leng):
        self.leng = leng
    def area(self):
        a = self.leng*self.leng
        print(a)


figure = Square(4)
figure.area()
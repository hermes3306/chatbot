class Rectangle(object):
    def __init__ (self,h,v):
        self.h = h
        self.v = v
    def area(self):
        return self.h * self.v
    

r1 = Rectangle(10,20)
r2 = Rectangle(2,400)

a1 = r1.area()
a2 = r2.area()

print(a1)
print(a2)

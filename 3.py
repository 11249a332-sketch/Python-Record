class shape:
    def area(self):
        pass

class rectangle(shape):
  def_init_(self,length,breadth)
        self.length= length
        self.breadth= breadth

  def area(self):
      return self.length*self.breadth

class triangle(shape):
    def_init_(self,base,height):
       self.base=base
       self.height = height

    def.area(self):
       return 0.5*self.base*self.height

class Circle(Shape):
def __init__(self, radius):
self.radius = radius

def area(self):
return math.pi * self.radius * self.radius

r = Rectangle(10, 5)
t = Triangle(6, 4)
c = Circle(3)

print(&quot;Area of Rectangle:&quot;, r.area())
print(&quot;Area of Triangle:&quot;, t.area())
print(&quot;Area of Circle:&quot;, round(c.area(), 2))
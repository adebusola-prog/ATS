# The world of shapes is much richer than the shapes included in the inheritance hierarchy of Fig. 9.3. 
# Write down all the shapes you can think of—both two-di- mensional and three-dimensional—and form them 
# into a more complete Shape hierarchy with as many levels as possible. Your hierarchy should have class Shape at the top.
#  Classes TwoDimension- alShape and ThreeDimensionalShape should extend Shape. Add additional subclasses, 
# such as Quad- rilateral and Sphere, at their correct locations in the hierarchy as necessary.


class Shape():
    def __init__(self, length):
        self.length = length
        
    def __str__(self):
        return self.length


class TwoDimensional(Shape):
    pass

class ThreeDimensional(Shape):
    pass


class Circle(TwoDimensional):
    pie = 3.142
    radius = 45
    def __init__(self, radius ,pie):
        self.pie = pie
        self.radius = radius
    
    def perimeter(self):
        return 2 * self.radius * self.pie  

    def area(self):
        return self.pie * self.radius ** 2


class Square(TwoDimensional):
    def perimeter(self):
        return self.length * 4

    def area(self):
        return self.length ** 2

class Rectangle(TwoDimensional):
    def perimeter(self, breadth = 9):
        self.breadth = breadth
        return  2 * (self.length + self.breadth)

    def area(self):
        return self.length * self.breadth


class RightTriangle(TwoDimensional):
    def __init__(self, hypothenus, base, height):
        self.hypothenus = hypothenus
        self.base = base
        self.height = height


    def perimeter(self):
        return self.base + self.height + self.hypothenus

    def area(self):
        return (1/2 * (self.base * self.height))

class Cube(ThreeDimensional):
    def __init__(self, length):
        super().__init__(length)

    def perimeter(self):
        return 12 * self.length

    def area(self):
        return 6 * (self.length**2)

    def volume(self):
        return self.length**3

class Sphere(ThreeDimensional):
    def __init__(self, pie, radius):

        self.pie = Circle.pie
        self.radius = Circle.radius

        # super().__init__(
        #     pie, radius
        # )
        # Circle.__init__(pie, radius)

    # def __str__(self):
    #     super().__str__(self)

    def perimeter(self):
        return 2 * self.radius * self.pie 

    def area(self):
        return 4 * self.pie * (self.radius**2)

    def volume(self):
        return 4/3 * self.pie * (self.radius**3)


class Tetrahedron(ThreeDimensional):
    def area(self):
        return 3**(1/2) * (self.length**2)

    def volume(self):
        return (self.length *(2**(1/3)))/12


class1 = Circle(7, 3.142)
print(class1.perimeter())
print(class1.area())
class2 = Square(8)
print(class2.perimeter())
print(class2.area())
class3 = Rectangle(9)
print(class3.perimeter())
print(class3.area())
class4 = RightTriangle(9, 7, 8)
print(class4.perimeter())
print(class4.area())
class5 = Cube(9)
print(class5.perimeter())
print(class5.volume())
print(class4.area())
class6 = Sphere(7, 3.142)
print(class6.perimeter())
print(class6.area())
class7 = Tetrahedron(8)
print(class7.volume())
print(class7.area())






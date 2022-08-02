class Shape:
    def __init__(self, radius, pie, length, breadth, height):
        self.radius = radius
        self.pie = pie
        self.length = length
        self.breadth = breadth
        self.height = height
        

class TwoDimensional:
    def two_dimensional(self):
        print("This is two dimensional")


class ThreeDimensional:
    def three_dimensional(self):
        print("this is three dimensional")


class Circle(Shape, TwoDimensional):
    def circle(self):
        area = self.pie * self.radius ** 2
        print(f"The area of a circle with radius-> {self.radius}m is {area}m2")


class Triangle(Shape, TwoDimensional):
    def right_triangle(self, base= 5):
        self.base = base
        area = (1/2) * self.base * self.height
        print(f"The area of a right-triangle with base->{self.base}m and ->height {self.height}m is {area}m2")


class Square(Shape, TwoDimensional):
    def square(self):
        area = self.length ** 2
        print(f"The area of a square with ->length {self.length}m is {area}m2")


class Sphere(Shape, ThreeDimensional):
    def sphere(self):
        area = 4 * self.pie * self.radius ** 2
        print(f"The area of a sphere with ->radius {self.radius}m is {area}m2")


class Cube(Shape, ThreeDimensional):
    def cube(self):
        area = 6 * self.length ** 2
        print(f"The area of a cube with ->length {self.length}m is {area}m2")


class Tetrahedron(Shape, ThreeDimensional):
    def tetra_hedron(self, edge=8):
        self.edge = edge
        area = (3 * self.edge **2) **(1/2)
        print(f"The area of a tetrahedron with ->edge {self.edge}m is {area}m2")


shape1 = Circle(7, 3.142, 8, 6, 9)
shape2 =Triangle(7, 3.142, 8, 6, 9)
shape3 = Square(7, 3.142, 8, 6, 9)
shape4 = Sphere(7, 3.142, 8, 6, 9)
shape5 = Cube(7, 3.142, 8, 6, 9)
shape6 = Tetrahedron(7, 3.142, 8, 6, 9)
shape1.circle()
shape2.right_triangle()
shape3.square()
shape4.sphere()
shape5.cube()
shape6.tetra_hedron()



# static method is independent of the class and the objet. when writing the function you pas in a normal arguement just like the normal function. and then you call it normally without using a function. 
# the importance is that it is used to test for whatever class you have created. you do not instatiate a static method when calling it. That is, you do not need to call using the object.
# In static method. you can place your function at the bootom or above the class as it is independent.

# In class method, you have to pass in an aguement called"cls". in the class method, you have to call the class. the class method helps us to write or get our items.
# example is when you create a csv file that stores your data. The class method is general to the class.



# CLASS AND INSTANCE
# class is like providing a default value to an item. when the class is passed in an object, the class could be called relative to the
# the object and a default value will be given to that object

# an instance is a unique argument that a function decides to carry aside the default arguement "self". it is unique to each object 
# and different object could be created from an instance. it is not a default like that of the class.































from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass
    

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        

    def calculate_area(self):
        return 3.14 * self.radius * self.radius
    
    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

circle = Circle(5)
print(f'Circle Area: {circle.calculate_area()}')
print(f'Circle Perimeter: {circle.calculate_perimeter()}')



class Square(Shape):
    def __init__(self,side):
        self.side = side

    def calculate_area(self):
        return self.side**2
    
    def calculate_perimeter(self):
        return 4 * self.side

square = Square(10)
print(f'Square Area: {square.calculate_area()}')
print(f'Circle Perimeter: {square.calculate_perimeter()}')



class Rectangle(Shape):
    def __init__(self,width,length):
        self.width = width
        self.length= length

    def calculate_area(self):
        return self.width * self.length
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.length)

rectangle = Rectangle(8,6)
print(f'Rectangle Area: {rectangle.calculate_area()}')
print(f' Rectangle Perimeter: {rectangle.calculate_perimeter()}')
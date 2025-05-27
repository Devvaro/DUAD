class Circle():
    radius=840


    def get_area(self):
        radius = Circle.radius/2
        result=radius ** 2
        area= result * 3.14
        print(f'the circle has a radius of {radius} and an area of {area}')


my_circle= Circle()
my_circle.get_area()

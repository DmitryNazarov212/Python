from math import *
class Figure:
    side_count = 0
    def __init__(self, color, *sides, filled = False):
        self.__sides = list((1 for i in range(0,self.side_count)))
        if self.__is_valid_sides(sides):
            self.__sides = list(sides)
    
        self.__color = list(color)

    def __is_valid_color(self, r,g,b):
        if (r >= 0 and r < 256) and (g >= 0 and g < 256) and (b >= 0 and b < 256):
            return True
        return False
    
    def set_color(self, r,g,b):
        if self.__is_valid_color(r,g,b):
            self.__color[0] = r
            self.__color[1] = g
            self.__color[2] = b
        else:
            self.__color = [0,0,0]

    def get_color(self):
        return self.__color
    
    def __is_valid_sides(self, args):
        for side in args:
            if side > 0 and len(args) == self.side_count: 
                return True
        return False

    def get_sides(self): 
        return self.__sides
    
    def set_sides(self, new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)
        else: 
            for i in range(self.side_count):
                self.__sides[i] = 1

class Circle(Figure):
    side_count = 1 
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0]/(2 * pi)
    
    def get_radius(self):
        return self.__radius
    def get_square(self):
        return pi * pow(self.__radius,2)
    
class Triangle(Figure):
    side_count = 3
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
    def get_square(self):
        p = (sum(list(self.get_sides())))/2
        return sqrt(p*((p - self.get_sides()[0])*(p - self.get_sides()[1])*(p - self.get_sides()[2])))

class Cube(Figure):
    side_count = 12
    def __init__(self, color, *sides):
        self.__sides = list((1 for i in range(0,self.side_count)))
        if len(sides) == 1:
            self.__sides = list((sides[0] for i in range(0,self.side_count)))
        super().__init__(color, *self.__sides)
    def get_volume(self):
        return pow(self.get_sides()[0], 3)


if __name__ == '__main__':

    figure = Figure((255, 0, 0), 5, 10, 15)
    figure.set_color(-1, 0, 2)

    print(figure.get_color())

    figure.set_color(252, 0, 252)

    print(figure.get_sides())
    print(figure.get_color())


    circle = Circle((255, 0, 0))
    print(circle.get_radius())
    print(circle.get_square())
    print(circle.get_sides())

    triangle = Triangle((0,0,0))
    print(triangle.get_sides())
    print(triangle.get_square())

    cube = Cube((2,3,5),1)
    print(cube.get_sides())
    print(cube.get_volume())

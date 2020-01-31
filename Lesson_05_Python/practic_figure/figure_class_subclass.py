"""Создание класса геом. фигуры и подклассов"""


class Figure():
    def __init__(self, name, angles, length_side):
        self.name = name
        self.angles = angles
        self.length_side = length_side

    def __str__(self):
        return "Фигура - {}, с кол-вом углов {}, длиной стороны {}".format(
            self.name, self.angles, self.length_side)

    def perimeter(self):
        perimeter = "Это периметр фигуры"
        return perimeter

    def area(self):
        area = "Это площадь фигуры"
        return area

    def add_square(self, other_figure, area, area_other):
        if isinstance(other_figure, Figure):
            print(area + area_other)
        else:
            print("Значение не определено в классе")


class Right_Triangle(Figure):
    def __init__(self, length_side, height):
        super().__init__(name="triangle", angles=3, length_side=length_side)
        self.height = height

    def __str__(self):
        return "Треугольник"

    def perimeter(self):
        perimeter = self.length_side * 3
        return perimeter

    def area(self):
        area_triangle = (self.length_side * self.height) * 0.5
        return area_triangle


class Square(Figure):
    def __init__(self, length_side):
        super().__init__(name="square", angles=4, length_side=length_side)

    def __str__(self):
        return "Квадрат"

    def perimeter(self):
        perimeter = self.length_side * 4
        return perimeter

    def area(self):
        area_square = self.length_side * self.length_side
        return area_square


class Rectangle(Figure):
    def __init__(self, length_side_1, length_side_2):
        super().__init__(name="rectangle", angles=4)
        self.length_side_1 = length_side_1
        self.length_side_2 = length_side_2

    def __str__(self):
        return "Прямоугольник"

    def perimeter(self):
        perimeter = (self.length_side_1 + self.length_side_2) * 2
        return perimeter

    def area(self):
        area_rectangle = self.length_side_1 * self.length_side_2
        return area_rectangle


class Circle(Figure):
    def __init__(self, circle_radius):
        super().__init__(name="circle", angles=None, length_side=circle_radius)

    def __str__(self):
        return "Круг"

    def circle_length(self):
        length_circle = 2 * self.length_side * 3.14
        return length_circle

    def area(self):
        area_circle = 3.14 * self.length_side * self.length_side
        return area_circle


cir = Circle(30)
tri = Right_Triangle(30, 10)

len_cir = cir.circle_length()
area_cir = cir.area()

per_tri = tri.perimeter()
area_tri = tri.area()

tri.add_square(cir, area_tri, area_cir)

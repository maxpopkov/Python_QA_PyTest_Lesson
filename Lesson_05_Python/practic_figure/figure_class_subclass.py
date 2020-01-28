"""Создание класса геом. фигуры и подклассов"""


class Figure():
    def __init__(self, name, angles, area, perimeter):
        self.name = name
        self.angles = angles
        self.area = area
        self.perimeter = perimeter

    def __str__(self):
        return "Фигура - {}, с кол-вом углов {}, площадью {}, периметром {}".format(
            self.name, self.angles, self.area, self.perimeter)

    def add_square(self, other_figure):
        if isinstance(other_figure, Figure):
            print(
                "Сумма площадей фигур {} и {}=".format(self.name, other_figure.name), self.area + other_figure.area)
        else:
            print("Значение не определено в классе")


class Triangle(Figure):
    def __init__(self, area, perimeter):
        super().__init__("triangle", 3, area, perimeter)

    def __str__(self):
        return "Треугольник, с площадью {}, периметром {}".format(
            self.area, self.perimeter)


class Square(Figure):
    def __init__(self, area, perimeter):
        super().__init__("square", 4, area, perimeter)

    def __str__(self):
        return "Квадрат, с площадью {}, периметром {}".format(
            self.area, self.perimeter)


class Rectangle(Figure):
    def __init__(self, area, perimeter):
        super().__init__("rectangle", 4, area, perimeter)

    def __str__(self):
        return "Прямоугольник, с площадью {}, периметром {}".format(
            self.area, self.perimeter)


class Circle(Figure):
    def __init__(self, area, perimeter):
        super().__init__("circle", None, area, perimeter)

    def __str__(self):
        return "Круг, с площадью {}, длиной окружности {}".format(
            self.area, self.perimeter)


cir_figure = Circle(30, 30)
tri_figure = Triangle(30, 30)
probe = "Тест"
cir_figure.add_square(tri_figure)
tri_figure.add_square(probe)

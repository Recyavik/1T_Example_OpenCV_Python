class Tetragon:
    name = 'Четырехугольник'
    def __init__(self, a=0, b=0, c=0, d=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimetr(self):
        perimetr = self.a + self.b + self.c + self.d
        return f'Периметр {self.name}: {perimetr}'

class Rectangle(Tetragon):
    def __init__(self, a, b):
        super().__init__(a, b, a, b)
        self.name = 'Прямоугольник'

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)
        self.name = 'Квадрат'

tetragon = Tetragon(10, 20, 30, 40)
print(tetragon.perimetr())

r = Rectangle(15, 20)
print(r.perimetr())

s = Square(40)
print(s.perimetr())
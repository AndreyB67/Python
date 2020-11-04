class ComplexChislo:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.cc = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма cc1 и cc2 равна')
        return f'cc = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение cc1 и cc2 равно')
        return f'cc = {self.a * other.a - (self.b * other.b)} + {self.b * other.a+self.a * other.b} * i'

    def __str__(self):
        return f'cc = {self.a} + {self.b} * i'


cc1 = ComplexChislo(1, -2)
cc2 = ComplexChislo(3, 4)
print(cc1)
print(cc2)
print(cc1 + cc2)
print(cc1 * cc2)
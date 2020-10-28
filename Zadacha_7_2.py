class Tkany:
    def __init__(self, size, height):
        self.size=size
        self.height=height


    def get_square_c(self):
        return self.size / 6.5 + 0.5

    def get_square_j(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Площадь общая ткани \n'
                   f' {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Palto(Tkany):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_c = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто {self.square_c}'


class Kostum(Tkany):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь на костюм {self.square_j}'


palto = Palto(2, 4)
kostum = Kostum(1, 2)
print(palto)
print(kostum)
print(palto.get_sq_full)
print(kostum.get_sq_full)
print(kostum.get_square_c())
print(kostum.get_square_j())

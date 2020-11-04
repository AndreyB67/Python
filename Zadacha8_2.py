class DelenieNaNull:
    def __init__(self, chislitel, znamenatel):
        self.chislitel = chislitel
        self.znamenatel = znamenatel

    @staticmethod
    def divide_by_null(chislitel, znamenatel):
        try:
            return (chislitel / znamenatel)
        except:
            return (f"Деление на ноль недопустимо")

div = DelenieNaNull(10, 100)
print(DelenieNaNull.divide_by_null(10, 10))
print(DelenieNaNull.divide_by_null(10, 0))
print(div.divide_by_null(100, 0))

class Car:
    year: str
    color: str
    price: float

    def __init__(self, year, color, price):
        self.year = year
        self.color = color
        self.price = price

    def calc_parcelas(self, parcelas):
        result = lambda x: (self.price / x)
        print(result(parcelas))

    def change_color(self, new_color):
        print(f"The old color is {self.color} and the new one will be {new_color}")
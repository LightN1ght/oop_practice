from src.base_product import BaseProduct
from src.logging_mixin import LoggingMixin


class Product(LoggingMixin, BaseProduct):
    name: str
    description: str
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    @classmethod
    def new_product(cls, product_data):
        return cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError
        else:
            return self.price * self.quantity + other.price * other.quantity

    def _repr_args(self):
        return self.name, self.description, self.price, self.quantity

    def __repr__(self):
        args = ", ".join(repr(value) for value in self._repr_args())
        return f"{type(self).__name__}({args})"

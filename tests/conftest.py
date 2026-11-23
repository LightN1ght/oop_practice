import pytest

from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture()
def product():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture()
def smartphone():
    return Smartphone(
        "Телефон", "Описание телефона", 100.0, 10, 95.5, "A1", 256, "Серый"
    )


@pytest.fixture()
def lawn_grass():
    return LawnGrass(
        "Газонная трава", "Описание травы", 500.0, 20, "Россия", "7 дней", "Зелёный"
    )

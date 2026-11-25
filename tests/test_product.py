import pytest

from src.base_product import BaseProduct
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_init_products(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_new_product():
    data = {"name": "Vivo", "description": "Синий", "price": 20000.0, "quantity": 14}
    product = Product.new_product(data)

    assert isinstance(product, Product)
    assert product.name == "Vivo"
    assert product.description == "Синий"
    assert product.price == 20000.0
    assert product.quantity == 14


def test_price_private(product):
    with pytest.raises(AttributeError):
        _ = product.__price


def test_price_increase(product, capsys):
    product.price = 200000.0

    assert product.price == 200000.0
    assert capsys.readouterr().out == ""


@pytest.mark.parametrize("invalid_price", [0, -5])
def test_price_rejects_nonpositive(product, invalid_price, capsys):
    old_price = product.price
    product.price = invalid_price

    assert product.price == old_price
    assert (
        capsys.readouterr().out.strip()
        == "Цена не должна быть нулевая или отрицательная"
    )


def test_product_str(product):
    assert str(product) == ("Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.")


def test_product_add():
    first = Product("Первый", "", 100, 10)
    second = Product("Второй", "", 200, 2)

    assert first + second == 1400


def test_smartphone_init(smartphone):
    assert isinstance(smartphone, Product)
    assert smartphone.name == "Телефон"
    assert smartphone.description == "Описание телефона"
    assert smartphone.price == 100.0
    assert smartphone.quantity == 10
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "A1"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"


def test_lawn_grass_init(lawn_grass):
    assert isinstance(lawn_grass, Product)
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.description == "Описание травы"
    assert lawn_grass.price == 500.0
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "7 дней"
    assert lawn_grass.color == "Зелёный"


def test_add_smartphones(smartphone):
    other = Smartphone("Другой телефон", "", 200.0, 2, 98.0, "B2", 512, "Белый")

    assert smartphone + other == 1400


def test_add_lawn_grass(lawn_grass):
    other = LawnGrass("Другая трава", "", 450.0, 15, "США", "5 дней", "Зелёный")

    assert lawn_grass + other == 16750


def test_add_different_subclasses(smartphone, lawn_grass):
    with pytest.raises(TypeError):
        _ = smartphone + lawn_grass


def test_add_product_and_subclass(product, smartphone):
    with pytest.raises(TypeError):
        _ = product + smartphone


def test_base_product_is_abstract():
    with pytest.raises(TypeError):
        BaseProduct()


def test_product_logs_creation(capsys):
    Product("Чай", "", 80, 15)

    assert capsys.readouterr().out == "Product('Чай', '', 80, 15)\n"


def test_product_rejects_zero_quantity():
    with pytest.raises(ValueError) as error:
        Product("Чай", "", 100, 0)

    assert str(error.value) == "Товар с нулевым количеством не может быть добавлен"

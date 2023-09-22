from src.item import Item
import pytest

"""Здесь надо написать тесты с использованием pytest для модуля item."""


@pytest.fixture()

def test_item():
    """создаем тестовый экземпляр"""
    return Item("Nokia", 1000, 1)


def test_calculate_total_price(test_item):
    """ тест функции общей стоимости продукции"""
    assert test_item.calculate_total_price() == 1000


def test_apply_discount(test_item):
    """тест скидки на цену товара"""
    assert test_item.apply_discount() == 1000

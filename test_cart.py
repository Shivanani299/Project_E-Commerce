import pytest
from cart import *


def test_add_valid_product():
    cart = {}
    result = add_to_cart(cart, "Laptop", 50000, 2)
    assert "Laptop" in result
    assert result["Laptop"]["quantity"] == 2


def test_add_invalid_quantity():
    cart = {}
    result = add_to_cart(cart, "Laptop", 50000, 0)
    assert result == "Invalid quantity"


def test_remove_existing_product():
    cart = {}
    add_to_cart(cart, "Laptop", 50000, 1)
    result = remove_from_cart(cart, "Laptop")
    assert "Laptop" not in result


def test_remove_non_existing_product():
    cart = {}
    result = remove_from_cart(cart, "Phone")
    assert result == "Product not in cart"


def test_calculate_total():
    cart = {}
    add_to_cart(cart, "Laptop", 50000, 2)
    add_to_cart(cart, "Mouse", 1000, 3)
    total = calculate_total(cart)
    assert total == 103000


def test_apply_discount_save10():
    assert apply_discount(1000, "SAVE10") == 900


def test_apply_invalid_coupon():
    assert apply_discount(1000, "INVALID") == 1000


def test_invalid_payment():
    assert validate_payment(1234, 12) == False


def test_valid_payment():
    assert validate_payment(1234567812345678, 123) == True


def test_place_order_empty_cart():
    cart = {}
    result = place_order(cart, 1234567812345678, 123)
    assert result == "Cart is empty"


def test_place_order_success():
    cart = {}
    add_to_cart(cart, "Laptop", 50000, 1)
    result = place_order(cart, 1234567812345678, 123)
    assert result == "Order placed successfully"
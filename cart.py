# ---------- Add to Cart ----------

def add_to_cart(cart, product, price, quantity):
    if quantity <= 0:
        return "Invalid quantity"

    if product in cart:
        cart[product]["quantity"] += quantity
    else:
        cart[product] = {
            "price": price,
            "quantity": quantity
        }

    return cart


def remove_from_cart(cart, product):
    if product not in cart:
        return "Product not in cart"

    del cart[product]
    return cart


def calculate_total(cart):
    total = 0
    for item in cart.values():
        total += item["price"] * item["quantity"]
    return total


def apply_discount(total, coupon):
    if coupon == "SAVE10":
        return total * 0.9
    return total


def validate_payment(card_number, cvv):
    if len(str(card_number)) == 16 and len(str(cvv)) == 3:
        return True
    return False


def place_order(cart, card_number, cvv):
    if not cart:
        return "Cart is empty"

    if not validate_payment(card_number, cvv):
        return "Payment failed"

    return "Order placed successfully"
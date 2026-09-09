"""Mini Store starter code for the Git/GitHub workflow exercise."""


def shipping_cost(subtotal):
    if subtotal < 0:
        raise ValueError("subtotal must be >= 0")
    return 99.0


def apply_discount(subtotal, percent):
    if subtotal < 0:
        raise ValueError("subtotal must be >= 0")
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    return round(subtotal * (1 - percent / 100), 2)


def can_checkout(item_count):
    return 1 <= item_count <= 50


def loyalty_discount(points):
    #This feature returns 0% below 500 points, 5% from 500–999, and 10% at 1000+ points.
    if points < 0:
        raise ValueError("points must be >= 0")
    if points < 500:
        return 0
    if points > 500 and points <= 999:
        return 5
    else:
        return 10
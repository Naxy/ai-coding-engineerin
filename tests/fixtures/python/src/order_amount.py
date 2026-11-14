from decimal import Decimal, ROUND_HALF_UP


def payable(unit_price: Decimal, quantity: int) -> Decimal:
    if unit_price < 0:
        raise ValueError("unit_price must be non-negative")
    if quantity < 0:
        raise ValueError("quantity must be non-negative")
    return (unit_price * quantity).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

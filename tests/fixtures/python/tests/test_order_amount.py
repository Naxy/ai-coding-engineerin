from decimal import Decimal
import pytest

from order_amount import payable


def test_payable_rounds_decimal_money():
    assert payable(Decimal("3.335"), 3) == Decimal("10.01")


@pytest.mark.parametrize("price,quantity", [(Decimal("-1"), 1), (Decimal("1"), -1)])
def test_payable_rejects_negative_inputs(price, quantity):
    with pytest.raises(ValueError):
        payable(price, quantity)

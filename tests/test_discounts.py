import pytest

from shopcart.discounts import (
    DiscountNotApplicableError,
    InvalidDiscountCodeError,
    apply_discount,
    get_discount,
)


def test_percent_discount():
    assert apply_discount(200.0, "LATO10") == pytest.approx(180.0)


def test_fixed_discount():
    assert apply_discount(100.0, "WITAJ20") == pytest.approx(80.0)


def test_min_total_not_met():
    with pytest.raises(DiscountNotApplicableError):
        apply_discount(100.0, "DUZE15")


def test_min_total_met():
    assert apply_discount(400.0, "DUZE15") == pytest.approx(340.0)


@pytest.mark.parametrize("code", ["lato10", "Lato10", "  LATO10  ", " lato10\t"])
def test_code_is_case_and_whitespace_insensitive(code):
    assert apply_discount(200.0, code) == pytest.approx(apply_discount(200.0, "LATO10"))


def test_unknown_code_has_readable_message():
    with pytest.raises(InvalidDiscountCodeError) as exc_info:
        apply_discount(100.0, "XYZ")
    assert str(exc_info.value) == "Nieznany kod rabatowy: XYZ"


def test_unknown_code_message_strips_whitespace():
    with pytest.raises(InvalidDiscountCodeError, match=r"^Nieznany kod rabatowy: XYZ$"):
        get_discount("  XYZ  ")

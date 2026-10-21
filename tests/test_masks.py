import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number_card, result",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("124578412549621", "Неверный номер карты"),
        ("", "Неверный номер карты"),
    ],
)
def test_get_mask_card_number(number_card, result):
    assert get_mask_card_number(number_card) == result


@pytest.mark.parametrize(
    "account, result",
    [
        ("73654108430135877777", "**7777"),
        ("123", "Неверный формат счёта"),
        ("", "Неверный формат счёта"),
        ("1234", "**1234"),
    ],
)
def test_get_mask_account(account, result):
    assert get_mask_account(account) == result

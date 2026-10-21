import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "name_card, result",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 700079228960 361", "Неверный номер карты"),
        ("Visa Platinum 700079228960636", "Неверный номер карты"),
    ],
)
def tests_mask_account_card(name_card, result):
    assert mask_account_card(name_card) == result


def tests_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"

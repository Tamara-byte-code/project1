"""Функции для маскировки банковских реквизитов."""


def get_mask_card_number(card_number: str) -> str:
    """Вернуть маску номера банковской карты."""
    if len(card_number) != 16:
        raise ValueError("Номер карты должен содержать ровно 16 символов")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Вернуть маску номера банковского счета. """
    if len(account_number) < 4:
        raise ValueError("Номер счета должен содержать не менее 4 символов")

    return f"**{account_number[-4:]}"

def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты.
    Пример: 7000792289606361 -> 7000 79** **** 6361
    """
    if len(card_number) != 16:
        return "Неверный номер карты"

    # Разбиваем на части по 4 цифры
    part1 = card_number[:4]
    part2 = card_number[4:6] + "**"
    part3 = "****"
    part4 = card_number[-4:]

    return f"{part1} {part2} {part3} {part4}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета, оставляя видимыми только последние 4 цифры.

    Args:
        account_number (str): Номер счета для маскировки

    Returns:
        str: Замаскированный номер счета
    """
    if not account_number:
        return ""

    # Очищаем строку от возможных пробелов и дефисов
    clean_number = account_number.replace(" ", "").replace("-", "")

    if len(clean_number) < 4:
        return "*" * len(clean_number)

    # Маскируем все символы, кроме последних 4
    masked = "*" * (len(clean_number) - 4) + clean_number[-4:]

    return masked
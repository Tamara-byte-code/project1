from masks import get_mask_card_number, get_mask_account


def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета.

    Принимает строку вида:
        "Visa Platinum 7000792289606361"
        "Maestro 7000792289606361"
        "Счет 73654108430135874305"

    Возвращает строку с замаскированным номером.
    """
    # Разделяем строку на две части: всё до последнего пробела — тип, после — номер
    *name_parts, number = info.rsplit(" ", 1)
    name = " ".join(name_parts)

    # Если тип — "Счет", используем маскировку счета, иначе — карты
    if name.lower().startswith("счет"):
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{name} {masked_number}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата "2024-03-11T02:26:18.671407"
    в формат "11.03.2024".
    """
    # Берем только часть до "T" и разбиваем по "-"
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"
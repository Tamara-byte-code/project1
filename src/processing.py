"""Функции для работы со списком банковских операций."""

from typing import Any


def filter_by_state(
    operations: list[dict[str, Any]], state: str = "EXECUTED"
) -> list[dict[str, Any]]:
    """Вернуть новый список операций с указанным статусом. """
    return [operation for operation in operations if operation.get("state") == state]


def sort_by_date(
    operations: list[dict[str, Any]], descending: bool = True
) -> list[dict[str, Any]]:
    """Вернуть новый список операций, отсортированный по дате."""
    return sorted(
        operations,
        key=lambda operation: str(operation["date"]),
        reverse=descending,
    )

"""Декоратор для логирования вызовов синхронных функций."""

from datetime import datetime, timezone
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

Parameters = ParamSpec("Parameters")
ReturnValue = TypeVar("ReturnValue")


def log(filename: str | None = None) -> Callable:
    """Логировать начало, результат или ошибку и завершение вызова."""

    def write_log(message: str) -> None:
        """Вывести сообщение в консоль или дописать его в выбранный файл."""
        if filename is None:
            print(message)
        else:
            with open(filename, "a", encoding="utf-8") as log_file:
                log_file.write(f"{message}\n")

    def decorator(function: Callable[Parameters, ReturnValue]) -> Callable:
        """Обернуть функцию логированием, сохранив ее метаданные."""

        @wraps(function)
        def wrapper(*args: Parameters.args, **kwargs: Parameters.kwargs) -> ReturnValue:
            """Вызвать функцию один раз и записать сведения о выполнении."""
            started_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
            input_values = f"{args!r}, {kwargs!r}"
            write_log(f"{function.__name__} start. Time: {started_at}. Inputs: {input_values}")
            try:
                result = function(*args, **kwargs)
            except Exception as error:
                write_log(
                    f"{function.__name__} error: {type(error).__name__}. "
                    f"Inputs: {input_values}. Error: {str(error)!r}"
                )
                raise
            else:
                write_log(f"{function.__name__} ok. Result: {result!r}")
                return result
            finally:
                finished_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
                write_log(f"{function.__name__} end. Time: {finished_at}")

        return wrapper

    return decorator

from typing import TypeVar, cast


T = TypeVar("T")


def validate_int(value: int, field_name: str) -> int:
    if not isinstance(value, int):
        raise TypeError(f"{field_name} must be an 'int' type")
    return value


def validate_positive(value: int, field_name: str) -> int:
    validate_int(value, field_name)
    if value <= 0:
        raise ValueError(f"{field_name} must be positive")
    return value


def validate_non_negative(value: int, field_name: str) -> int:
    validate_int(value, field_name)
    if value < 0:
        raise ValueError(f"{field_name} must be non-negative")
    return value


def validate_instance(
    value: object,
    expected_type: type[T],
    field_name: str,
) -> T:
    if not isinstance(value, expected_type):
        raise TypeError(f"{field_name} must be a '{expected_type.__name__}' instance")
    return cast(T, value)

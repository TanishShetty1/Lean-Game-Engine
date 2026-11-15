from dataclasses import dataclass

from .validation import validate_int, validate_positive


@dataclass
class Speed:
    _base_speed: int
    _current_speed: int

    def __post_init__(self) -> None:
        self._base_speed = validate_positive(self._base_speed, "BASE-SPEED")
        self._current_speed = validate_positive(
            self._current_speed,
            "CURRENT-SPEED",
        )

    @property
    def base_speed(self) -> int:
        return self._base_speed

    @base_speed.setter
    def base_speed(self, value: int) -> None:
        self._base_speed = validate_positive(value, "BASE-SPEED")

    @property
    def current_speed(self) -> int:
        return self._current_speed

    @current_speed.setter
    def current_speed(self, value: int) -> None:
        self._current_speed = validate_positive(value, "CURRENT-SPEED")

    def reset_current_speed_to_base(self) -> None:
        self._current_speed = self._base_speed

    def _increase_current_speed(self, increment: int) -> None:
        increment = validate_int(increment, "INCREMENT")
        if increment <= 0:
            return
        self._current_speed += increment

    def _decrease_current_speed(self, decrement: int) -> None:
        decrement = validate_int(decrement, "DECREMENT")
        if decrement <= 0:
            return
        self._current_speed = max(1, self._current_speed - decrement)

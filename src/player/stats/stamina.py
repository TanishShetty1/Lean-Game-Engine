from dataclasses import dataclass

from .validation import validate_non_negative, validate_positive


@dataclass
class Stamina:
    _max_physical_stamina: int
    _current_physical_stamina: int
    _max_special_stamina: int
    _current_special_stamina: int

    def __post_init__(self) -> None:
        self._max_physical_stamina = validate_positive(
            self._max_physical_stamina,
            "MAX-PHYSICAL-STAMINA",
        )
        self._current_physical_stamina = validate_positive(
            self._current_physical_stamina,
            "CURRENT-PHYSICAL-STAMINA",
        )
        self._max_special_stamina = validate_positive(
            self._max_special_stamina,
            "MAX-SPECIAL-STAMINA",
        )
        self._current_special_stamina = validate_positive(
            self._current_special_stamina,
            "CURRENT-SPECIAL-STAMINA",
        )

    @property
    def max_physical_stamina(self) -> int:
        return self._max_physical_stamina

    @max_physical_stamina.setter
    def max_physical_stamina(self, value: int) -> None:
        self._max_physical_stamina = validate_positive(
            value,
            "MAX-PHYSICAL-STAMINA",
        )

    @property
    def max_special_stamina(self) -> int:
        return self._max_special_stamina

    @max_special_stamina.setter
    def max_special_stamina(self, value: int) -> None:
        self._max_special_stamina = validate_positive(
            value,
            "MAX-SPECIAL-STAMINA",
        )

    @property
    def current_physical_stamina(self) -> int:
        return self._current_physical_stamina

    @current_physical_stamina.setter
    def current_physical_stamina(self, value: int) -> None:
        self._current_physical_stamina = validate_non_negative(
            value,
            "CURRENT-PHYSICAL-STAMINA",
        )

    @property
    def current_special_stamina(self) -> int:
        return self._current_special_stamina

    @current_special_stamina.setter
    def current_special_stamina(self, value: int) -> None:
        self._current_special_stamina = validate_non_negative(
            value,
            "CURRENT-SPECIAL-STAMINA",
        )

    def reset_current_physical_stamina(self) -> None:
        self._current_physical_stamina = self._max_physical_stamina

    def reset_current_special_stamina(self) -> None:
        self._current_special_stamina = self._max_special_stamina

    def increase_current_physical_stamina(self, increment: int) -> int:
        increment = validate_non_negative(increment, "INCREMENT")
        increased = min(
            increment,
            self._max_physical_stamina - self._current_physical_stamina,
        )
        self._current_physical_stamina += increased
        return increased

    def decrease_current_physical_stamina(self, decrement: int) -> int:
        decrement = validate_non_negative(decrement, "DECREMENT")
        decreased = min(decrement, self._current_physical_stamina)
        self._current_physical_stamina -= decreased
        return decreased

    def increase_current_special_stamina(self, increment: int) -> int:
        increment = validate_non_negative(increment, "INCREMENT")
        increased = min(
            increment,
            self._max_special_stamina - self._current_special_stamina,
        )
        self._current_special_stamina += increased
        return increased

    def decrease_current_special_stamina(self, decrement: int) -> int:
        decrement = validate_non_negative(decrement, "DECREMENT")
        decreased = min(decrement, self._current_special_stamina)
        self._current_special_stamina -= decreased
        return decreased

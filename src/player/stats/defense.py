from dataclasses import dataclass

from .validation import validate_int, validate_positive
@dataclass
class Defense:
    _base_physical_defense: int
    _modifier_physical_defense: int
    _base_special_defense: int
    _modifier_special_defense: int

    def __post_init__(self):
        self._base_physical_defense = validate_positive(
            self._base_physical_defense,
            "BASE-PHYSICAL-DEFENSE",
        )
        self._base_special_defense = validate_positive(
            self._base_special_defense,
            "BASE-SPECIAL-DEFENSE",
        )
        self._modifier_physical_defense = validate_int(
            self._modifier_physical_defense,
            "MODIFIER-PHYSICAL-DEFENSE",
        )
        self._modifier_special_defense = validate_int(
            self._modifier_special_defense,
            "MODIFIER-SPECIAL-DEFENSE",
        )

    @property
    def base_physical_defense(self) -> int:
        return self._base_physical_defense

    @base_physical_defense.setter
    def base_physical_defense(self, value: int) -> None:
        self._base_physical_defense = validate_positive(
            value,
            "BASE-PHYSICAL-DEFENSE",
        )

    @property
    def base_special_defense(self) -> int:
        return self._base_special_defense

    @base_special_defense.setter
    def base_special_defense(self, value: int) -> None:
        self._base_special_defense = validate_positive(
            value,
            "BASE-SPECIAL-DEFENSE",
        )

    @property
    def modifier_physical_defense(self) -> int:
        return self._modifier_physical_defense

    @modifier_physical_defense.setter
    def modifier_physical_defense(self, value: int) -> None:
        self._modifier_physical_defense = validate_int(
            value,
            "MODIFIER-PHYSICAL-DEFENSE",
        )

    @property
    def modifier_special_defense(self) -> int:
        return self._modifier_special_defense

    @modifier_special_defense.setter
    def modifier_special_defense(self, value: int) -> None:
        self._modifier_special_defense = validate_int(
            value,
            "MODIFIER-SPECIAL-DEFENSE",
        )

    @property
    def current_physical_defense(self) -> int:
        return self._base_physical_defense + self._modifier_physical_defense

    @property
    def current_special_defense(self) -> int:
        return self._base_special_defense + self._modifier_special_defense


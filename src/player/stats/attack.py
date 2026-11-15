from dataclasses import dataclass

from .validation import validate_int, validate_non_negative

@dataclass
class Attack:
    _base_physical_attack: int
    _modifier_physical_attack: int
    _base_special_attack: int
    _modifier_special_attack: int

    def __post_init__(self):
        self._base_physical_attack = validate_non_negative(
            self._base_physical_attack,
            "BASE-PHYSICAL-ATTACK",
        )
        self._modifier_physical_attack = validate_int(
            self._modifier_physical_attack,
            "MODIFIER-PHYSICAL-ATTACK",
        )
        self._base_special_attack = validate_non_negative(
            self._base_special_attack,
            "BASE-SPECIAL-ATTACK",
        )
        self._modifier_special_attack = validate_int(
            self._modifier_special_attack,
            "MODIFIER-SPECIAL-ATTACK",
        )

    @property
    def base_physical_attack(self) -> int:
        return self._base_physical_attack

    @base_physical_attack.setter
    def base_physical_attack(self, value: int) -> None:
        self._base_physical_attack = validate_non_negative(value, "BASE-PHYSICAL-ATTACK")

    @property
    def base_special_attack(self) -> int:
        return self._base_special_attack

    @base_special_attack.setter
    def base_special_attack(self, value: int) -> None:
        self._base_special_attack = validate_non_negative(value, "BASE-SPECIAL-ATTACK")

    @property
    def modifier_physical_attack(self) -> int:
        return self._modifier_physical_attack

    @modifier_physical_attack.setter
    def modifier_physical_attack(self, value: int) -> None:
        self._modifier_physical_attack = validate_int(value, "MODIFIER-PHYSICAL-ATTACK")

    @property
    def modifier_special_attack(self) -> int:
        return self._modifier_special_attack

    @modifier_special_attack.setter
    def modifier_special_attack(self, value: int) -> None:
        self._modifier_special_attack = validate_int(value, "MODIFIER-SPECIAL-ATTACK")

    @property
    def current_physical_attack(self) -> int:
        return self._base_physical_attack + self._modifier_physical_attack

    @property
    def current_special_attack(self) -> int:
        return self._base_special_attack + self._modifier_special_attack

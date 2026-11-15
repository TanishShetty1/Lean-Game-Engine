from dataclasses import dataclass

from .validation import validate_non_negative, validate_positive


@dataclass
class Health:
    _max_health: int
    _hit_points: int

    def __post_init__(self) -> None:
        self._max_health = validate_positive(self._max_health, "MAX-HEALTH")
        self._hit_points = min(
            validate_non_negative(self._hit_points, "HIT-POINTS"),
            self._max_health,
        )

    @property
    def max_health(self) -> int:
        return self._max_health

    @max_health.setter
    def max_health(self, value: int) -> None:
        value = validate_positive(value, "MAX-HEALTH")
        self._max_health = value
        self._hit_points = min(self._hit_points, value)

    @property
    def hit_points(self) -> int:
        return self._hit_points

    @hit_points.setter
    def hit_points(self, value: int) -> None:
        self._hit_points = min(
            validate_non_negative(value, "HIT-POINTS"),
            self._max_health,
        )

    @property
    def has_hit_points_left(self) -> bool:
        return self._hit_points > 0

    def increment_hit_points(self, increment: int) -> int:
        increment = validate_non_negative(increment, "INCREMENT")
        increased = min(increment, self._max_health - self._hit_points)
        self._hit_points += increased
        return increased

    def decrement_hit_points(self, decrement: int) -> int:
        decrement = validate_non_negative(decrement, "DECREMENT")
        decreased = min(decrement, self._hit_points)
        self._hit_points -= decreased
        return decreased

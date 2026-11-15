from dataclasses import dataclass

from .attack import Attack
from .defense import Defense
from .health import Health
from .speed import Speed
from .stamina import Stamina
from .validation import validate_instance


@dataclass
class Stats:
    _attack: Attack
    _defense: Defense
    _health: Health
    _speed: Speed
    _stamina: Stamina

    def __post_init__(self) -> None:
        self._attack = validate_instance(self._attack, Attack, "attack")
        self._defense = validate_instance(self._defense, Defense, "defense")
        self._health = validate_instance(self._health, Health, "health")
        self._speed = validate_instance(self._speed, Speed, "speed")
        self._stamina = validate_instance(self._stamina, Stamina, "stamina")

    @property
    def attack(self) -> Attack:
        return self._attack

    @attack.setter
    def attack(self, value: Attack) -> None:
        self._attack = validate_instance(value, Attack, "attack")

    @property
    def defense(self) -> Defense:
        return self._defense

    @defense.setter
    def defense(self, value: Defense) -> None:
        self._defense = validate_instance(value, Defense, "defense")

    @property
    def health(self) -> Health:
        return self._health

    @health.setter
    def health(self, value: Health) -> None:
        self._health = validate_instance(value, Health, "health")

    @property
    def speed(self) -> Speed:
        return self._speed

    @speed.setter
    def speed(self, value: Speed) -> None:
        self._speed = validate_instance(value, Speed, "speed")

    @property
    def stamina(self) -> Stamina:
        return self._stamina

    @stamina.setter
    def stamina(self, value: Stamina) -> None:
        self._stamina = validate_instance(value, Stamina, "stamina")


def initialize_player_stats(stat_dict: dict[str, int]) -> Stats:
    attack = Attack(
        stat_dict["base_physical_attack"],
        0,
        stat_dict["base_special_attack"],
        0,
    )
    defense = Defense(
        stat_dict["base_physical_defense"],
        0,
        stat_dict["base_special_defense"],
        0,
    )
    health = Health(stat_dict["max_health"], stat_dict["max_health"])
    speed = Speed(stat_dict["base_speed"], stat_dict["base_speed"])
    stamina = Stamina(
        stat_dict["max_physical_stamina"],
        stat_dict["max_physical_stamina"],
        stat_dict["max_special_stamina"],
        stat_dict["max_special_stamina"],
    )
    return Stats(attack, defense, health, speed, stamina)

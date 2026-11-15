import logging
from uuid import uuid4

from .archetype import BASE_STATS, PlayerClass
from .stats.stats import Stats, initialize_player_stats

logger = logging.getLogger(__name__)

_FALLBACK_NAME = "MISSING_NAME"


class Player:
    def __init__(self, name: str, stats: Stats) -> None:
        self._uid = uuid4()
        self._name = self._set_player_name(name)
        self._stats = self._set_player_stats(stats)
        self._alive = True

    @property
    def uid(self):
        return self._uid

    @property
    def name(self) -> str:
        return self._name

    @property
    def stats(self) -> Stats:
        return self._stats

    @property
    def is_alive(self) -> bool:
        return self._alive

    @staticmethod
    def _set_player_name(name: str) -> str:
        if isinstance(name, str) and name.strip():
            return name

        logger.warning("Invalid player name %r; assigning fallback name", name)
        return _FALLBACK_NAME

    @staticmethod
    def _set_player_stats(stats: Stats) -> Stats:
        if not isinstance(stats, Stats):
            emsg = f"{stats} must be a 'Stats' instance"
            logger.error(emsg)
            raise TypeError(emsg)
        return stats

    def _apply_damage(self, attack: int, defense: int) -> None:
        if not isinstance(attack, int):
            raise TypeError("attack must be an 'int' type")
        if attack < 0:
            raise ValueError("attack must be non-negative")

        damage = max(0, attack - defense)
        if damage:
            self._stats.health.decrement_hit_points(damage)
            self._alive = self._stats.health.has_hit_points_left

        logger.info("%s took damage worth %s", self, damage)

    def handle_physical_attack(self, physical_attack: int) -> None:
        defense = self._stats.defense.current_physical_defense
        self._apply_damage(physical_attack, defense)

    def handle_special_attack(self, special_attack: int) -> None:
        defense = self._stats.defense.current_special_defense
        self._apply_damage(special_attack, defense)

    def __repr__(self) -> str:
        return f"Player(name={self._name!r}, uid={self._uid})"


def initialize_player(name: str, player_class: PlayerClass) -> Player:
    stats = initialize_player_stats(BASE_STATS[player_class])
    return Player(name, stats)


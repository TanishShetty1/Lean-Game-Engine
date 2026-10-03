import logging

from dataclasses import dataclass
from health import Health
from speed import Speed
from defense import Defense

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Stats:
    _health : Health
    _defense : Defense
    _speed : Speed


    @property 
    def health(self)->Health:
        return self._health

    @health.setter
    def health(self,health:Health)->None:
        if not isinstance(health,Health):
            emsg = f"{health} is not a 'Health' instance"
            logger.error(emsg)
            raise TypeError(emsg)
        self._health = health

    @property
    def defense(self)->Defense:
        return self._defense

    @defense.setter
    def defense(self,defense:Defense)->None:
        if not isinstance(defense,Defense):
            emsg = f"{defense} is not a 'Defense' instance"
            logger.error(emsg)
            raise TypeError(emsg)
        self._defense = defense

    @property
    def speed(self)->Speed:
        return self._speed

    @speed.setter
    def speed(self,speed:Speed)->None:
        if not isinstance(speed,Speed):
            emsg = f"{speed} is not a 'Speed' instance"
            logger.error(emsg)
            raise TypeError(emsg)
        self._speed = speed
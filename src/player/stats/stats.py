import logging

from dataclasses import dataclass
from health import Health
from speed import Speed

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Stats:
    _health : Health
    _speed : Speed

    @property 
    def health(self)->Health:
        return self._health

    @health.setter
    def health(self,health:Health)->None:
        if not isinstance(health,Health):
            emsg = f"{health} must be an 'Health' instance"
            logger.error(emsg)
            raise TypeError(emsg)
        self._health = health

    @property
    def speed(self)->Speed:
        return self._speed

    @speed.setter
    def speed(self,speed:Speed)->None:
        if not isinstance(speed,Speed):
            emsg = f"{speed} must be a 'Speed' instance"
            logger.error(emsg)
            raise TypeError(emsg)
        self._speed = speed
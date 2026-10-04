import logging

from dataclasses import dataclass
from attack import Attack
from defense import Defense
from health import Health
from speed import Speed
from stamina import Stamina

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Stats:
    _attack : Attack
    _defense : Defense
    _health : Health
    _speed : Speed
    _stamina : Stamina

    @property
    def attack(self)->Attack:
        return self._attack

    @attack.setter
    def attack(self,attack:Attack)->None:
        if not isinstance(attack,Attack):
            emsg = f"{attack} must be an 'Attack' instance"
            logger.error(emsg)
            raise TypeError(emsg)

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
    def speed(self)->Speed:
        return self._speed

    @speed.setter
    def speed(self,speed:Speed)->None:
        if not isinstance(speed,Speed):
            emsg = f"{speed} is not a 'Speed' instance"
            logger.error(emsg)
            raise TypeError(emsg)
        self._speed = speed

    @property
    def stamina(self)->Stamina:
        return self._stamina

    @stamina.setter
    def stamina(self,stamina:Stamina)->None:
        if not isinstance(stamina,Stamina):
            emsg = f"{stamina} is not a 'Stamina' instance"
            logger.error(emsg)
            raise TypeError(emsg)
        self._stamina = stamina
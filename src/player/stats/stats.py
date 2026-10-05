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

def initialize_player_stats(stat_dict:dict[str,int])->Stats:

    attack = Attack(stat_dict["base_physical_attack"],
                    stat_dict["modifier_physical_attack"],
                    stat_dict["base_special_attack"],
                    stat_dict["modifier_special_attack"])

    defense = Defense(stat_dict["base_physical_defense"],
                    stat_dict["modifier_physical_defense"],
                    stat_dict["base_special_defense"],
                    stat_dict["modifier_special_defense"])

    health = Health(stat_dict["max_health"],
                    stat_dict["hit_points"])

    speed = Speed(stat_dict["base_speed"],
                  stat_dict["current_speed"])
    
    stamina = Stamina(stat_dict["max_physical_stamina"],
                      stat_dict["current_physical_stamina"],
                      stat_dict["max_special_stamina"],
                      stat_dict["current_special_stamina"])

    stats = Stats(attack,defense,health,speed,stamina)

    return stats
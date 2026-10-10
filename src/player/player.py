import logging
from src.player.stats.stats import Stats,initialize_player_stats
from src.player.archetype import PlayerClass,BASE_STATS
from stats.stats import Stats,initialize_player_stats
from archetype import PlayerClass,BASE_STATS
from uuid import uuid4

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)


_FALLBACK_NAME = "MISSING_NAME"

class Player:
    def __init__(self,name:str,stats:Stats):
        self._uid = uuid4()
        self._name = self._set_player_name(name)
        self._stats = self._set_player_stats(stats)
        self._alive = True

    def _set_player_name(self,name:str):

        if isinstance(name,str) and name!=" ":
            return name

        #TODO implement a way to assign a random unique name
        if not isinstance(name,str):
            msg = "{name} is not a string instance, assigning a random name"
        else:
            msg = "Empty string entered, assigning a random name"

        logger.warning(msg)
        return _FALLBACK_NAME

    def _set_player_stats(self,stats:Stats)->Stats:
        if not isinstance(stats,Stats):
            emsg = f"{stats} must be a 'Stats' instance"
            logger.error(emsg)
            raise TypeError(emsg)
        return stats

    #interaction methods :
    def handle_physical_attack(self,physical_attack:int)->None:
        player_physical_defense = self._stats._defense.current_physical_defense
        damage = max(0,physical_attack-player_physical_defense)
        if damage>0 :
            msg = f"{self.__repr__()} took damage worth {damage}"
            self._stats.health.decrement_hit_points(damage)
            #TODO: handle scenario where the player dies
        else :
            msg = f"{self.__repr__()} took no damage"
        logger.info(msg)

    def handle_special_attack(self,special_attack:int)->None:
        player_special_defense = self. _stats._defense._base_special_defense
        damage = max(0,special_attack - player_special_defense)
        if damage>0 :
            msg = f"{self.__repr__()} took damage worth {damage}"
            self._stats.health.decrement_hit_points(damage)
            #TODO: handle scenario where the player dies
        else :
            msg = f"{self.__repr__()} took no damage"
        logger.info(msg)

def initialize_player(name:str,player_class:PlayerClass)->Player:
    stat_dict = BASE_STATS[player_class]
    stats = initialize_player_stats(stat_dict)
    player = Player(name,stats)
    return player


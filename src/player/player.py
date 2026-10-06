import logging
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

    def _set_player_stats(self,stats:Stats)->None:
        if not isinstance(stats,Stats):
            emsg = f"{stats} must be a 'Stats' instance"
            logger.error(emsg)
            raise TypeError(emsg)
        self._stats = stats

def initialize_player(name:str,player_class:PlayerClass)->Player:
    stat_dict = BASE_STATS[player_class]
    stats = initialize_player_stats(stat_dict)
    player = Player(name,stats)
    return player
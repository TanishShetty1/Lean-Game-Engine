import logging
from uuid import uuid4


logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)


_FALLBACK_NAME = "MISSING_NAME"


class Player:
    def __init__(self,name:str):
        self._uid = uuid4()
        self._name = self._set_player_name(name)
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
    
    

    
import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Stamina:
    _max_physical_stamina:int
    _current_physical_stamina:int
    _max_special_stamina:int
    _current_special_stamina:int

    #implement __post_init__()
    @property
    def max_physical_stamina(self)->int:
        return self._max_physical_stamina

    @max_physical_stamina.setter
    def max_physical_stamina(self,max_physical_stamina)->None:
        if not isinstance(max_physical_stamina,int):
            emsg = "MAX_PHYSICAL_STAMINA must be an 'int' type"
            logger.error(emsg)
            raise TypeError(emsg)
        self._max_physical_stamina = max_physical_stamina

    @property
    def max_special_stamina(self)->int:
        return self._max_special_stamina

    @max_special_stamina.setter
    def max_special_stamina(self,max_special_stamina)->None:
        if not isinstance(max_special_stamina,int):
            emsg = "MAX_SPECIAL_STAMINA must be an 'int' type"
            logger.error(emsg)
            raise TypeError(emsg)
        self._max_special_stamina = max_special_stamina

    @property
    def current_physical_stamina(self)->int:
        return self._current_physical_stamina

    @current_physical_stamina.setter
    def current_physical_stamina(self,current_physical_stamina)->None:
        if not isinstance(current_physical_stamina,int):
            emsg = "CURRENT_PHYSICAL_STAMINA must be an 'int' type"
            logger.error(emsg)
            raise TypeError(emsg)
        self._current_physical_stamina = current_physical_stamina

    @property
    def current_special_stamina(self)->int:
        return self._current_special_stamina

    @current_special_stamina.setter
    def current_special_stamina(self,current_special_stamina)->None:
        if not isinstance(current_special_stamina,int):
            emsg = "CURRENT_SPECIAL_STAMINA must be an 'int' type"
            logger.error(emsg)
            raise TypeError(emsg)
        self._current_special_stamina = current_special_stamina

    #implement interaction methods




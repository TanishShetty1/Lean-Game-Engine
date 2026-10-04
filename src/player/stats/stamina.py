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

    def __post_init__(self):
        if self._max_physical_stamina<=0:
            emsg = "MAX-PHYSICAL-STAMINA must be positve"
            logger.error(emsg)
            raise ValueError(emsg)

        if self._max_special_stamina<=0:
            emsg = "MAX-SPECIAL-STAMINA must be positve"
            logger.error(emsg)
            raise ValueError(emsg)

        if self._current_physical_stamina<=0:
            emsg = "CURRENT-PHYSICAL-STAMINA must be positve"
            logger.error(emsg)
            raise ValueError(emsg)

        if self._current_special_stamina<=0:
            emsg = "CURRENT-PHYSICAL-STAMINA must be positve"
            logger.error(emsg)
            raise ValueError(emsg)


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

    def reset_current_physical_stamina(self)->None:
        self._current_physical_stamina = self._max_physical_stamina

    def reset_current_special_stamina(self)->None:
        self._current_special_stamina = self._max_special_stamina

    def increase_current_physical_stamina(self,increment)->int:
        if increment<0 :
            emsg = f"Increment must be non-negative"
            logger.error(emsg)
            raise ValueError(emsg)

        initial = self._current_physical_stamina
        incremented_value = min(increment,self._max_physical_stamina-initial)
        self._current_physical_stamina += incremented_value
        imsg = f"current_physical_stamina increased from {initial}->{self._current_physical_stamina}"
        logger.info(imsg)
        return incremented_value

    def decrease_current_physical_stamina(self,decrement)->int:
        if decrement<0 :
            emsg = f"decrement must be non-negative"
            logger.error(emsg)
            raise ValueError(emsg)

        initial = self._current_physical_stamina
        decremented_value = min(decrement,initial)
        self._current_physical_stamina -= decremented_value
        imsg = f"current_physical_stamina decreased from {initial}->{self._current_physical_stamina}"
        logger.info(imsg)
        return decremented_value

    def increase_current_special_stamina(self,increment)->int:
        if increment<0 :
            emsg = f"Increment must be non-negative"
            logger.error(emsg)
            raise TypeError(emsg)

        initial = self._current_special_stamina
        incremented_value = min(increment,self._max_special_stamina-initial)
        self._current_special_stamina += incremented_value
        imsg = f"current_special_stamina increased from {initial}->{self._current_special_stamina}"
        logger.info(imsg)
        return incremented_value

    def decrease_current_special_stamina(self,decrement)->int:
        if decrement<0 :
            emsg = f"decrement must be non-negative"
            logger.error(emsg)
            raise ValueError(emsg)

        initial = self._current_special_stamina
        decremented_value = min(decrement,initial)
        self._current_special_stamina -= decremented_value
        imsg = f"current_special_stamina decreased from {initial}->{self._current_special_stamina}"
        logger.info(imsg)
        return decremented_value

    




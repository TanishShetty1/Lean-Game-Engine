import logging
from dataclasses import dataclass

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Speed:
    _base_speed:int
    _current_speed:int

    def __post_init__(self):
        if self._base_speed <= 0:
            emsg = "BASE-SPEED must be positive"
            logger.error(emsg)
            raise ValueError(emsg)

        if self._current_speed <= 0:
            emsg = "CURRENT-SPEED must be positive"
            logger.error(emsg)
            raise ValueError(emsg)


    #getters and setters :
    @property
    def base_speed(self):
        return self._base_speed

    @base_speed.setter
    def base_speed(self,base_speed:int)->None:
        if not isinstance(base_speed,int):
            emsg = "BASE-SPEED must be an 'int' type"
            logger.error(emsg)
            raise TypeError(emsg)
        self._base_speed = base_speed

    @property
    def current_speed(self)->int:
        return self._current_speed

    @current_speed.setter
    def current_speed(self,current_speed:int)->None:
        if not isinstance(current_speed,int):
            emsg = "CURRENT-SPEED must be an 'int' type"
            logger.error(emsg)
            raise TypeError(emsg)
        self._current_speed = current_speed


    #interaction methods :
    def reset_current_speed_to_base(self):
        initial_speed = self._current_speed
        self._current_speed = self._base_speed
        imsg = f"CURRENT-SPEED reset from {initial_speed}->{self._current_speed}"
        logger.info(imsg)
    
    #TODO ponder about what this function should return
    def _increase_current_speed(self,increment:int)->None:
        if increment<=0:
            wmsg = "INCREMENT amount must be positive"
            logger.warning(wmsg)
            return
        
        initial_speed = self._current_speed
        self._current_speed += increment
        imsg = f"CURRENT-SPEED increased from {initial_speed}->{self._current_speed}"
        logger.info(imsg)

    def _decrease_current_speed(self,decrement:int)->None:
        if decrement<=0:
            wmsg = "DECREMENT amount must be positive"
            logger.warning(wmsg)
            return

        initial_speed = self._current_speed
        self._current_speed = max(1,initial_speed - decrement)
        imsg = f"CURRENT-SPEED decreased from {initial_speed}->{self._current_speed}"
        logger.info(imsg)



        

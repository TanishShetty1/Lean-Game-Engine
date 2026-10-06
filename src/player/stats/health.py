import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Health:
    _max_health:int
    _hit_points:int

    def __post_init__(self)->None:
        if(self._max_health<=0):
            emsg = "MAX-HEALTH cannot be initialized with a non positive value"
            logger.error(emsg)
            raise ValueError(emsg)

        if(self._hit_points<0):
            emsg = "HIT-POINTS cannot be initialized with a non positive value"
            logger.error(emsg)
            raise ValueError(emsg)

        if(self._hit_points>self._max_health):
            emsg = (f"HIT-POINTS({self._hit_points}) cannot exceed MAX-HEALTH({self._max_health}) " 
                   f"HIT-POINTS {self._hit_points}->{self._max_health}")
            logger.warning(emsg)
            self._hit_points = self._max_health


    #getter and setters : 
    @property
    def max_health(self)->int:
        return self._max_health

    @max_health.setter
    def max_health(self,max_health:int)->None:
        if not isinstance(max_health,int):
            emsg = "MAX-HEALTH must be an 'int' type"
            logger.error(emsg)
            raise TypeError(emsg)
        self._max_health = max_health
        return

    @property
    def hit_points(self):
        return self._hit_points

    @hit_points.setter
    def hit_points(self,hit_points:int)->None:
        if not isinstance(hit_points,int):
            emsg = "HIT-POINTS must be an 'int' type"
            logger.error(emsg)
            raise TypeError(emsg)
        self._hit_points = hit_points
        return


    #interaction methods:
    def _has_hit_points_left(self):
        return self._hit_points>0


    def increment_hit_points(self,increment:int)->int:
        if not isinstance(increment,int):
            emsg = f"{increment} must be an 'int' type"
            logger.error(emsg)
            raise TypeError(emsg)
        initial_hp = self._hit_points
        increased_hp = min(increment,self._max_health-initial_hp)
        self._hit_points += increased_hp
        msg = f"HIT-POINTS increased from {initial_hp}->{self._hit_points}"
        logger.info(msg)
        return increased_hp


    def decrement_hit_points(self,decrement:int)->int:
            if not isinstance(decrement,int):
                emsg = f"{decrement} must be an 'int' type"
                logger.error(emsg)
                raise TypeError(emsg)
            initial_hp = self._hit_points
            decreased_hp = min(decrement,self._hit_points)
            self._hit_points -= decreased_hp
            msg = f"HIT-POINTS decreased from {initial_hp}->{self._hit_points}"
            logger.info(msg)
            return decreased_hp
    
import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Defense:
    _base_physical_defense : int
    _base_special_defense : int
    _modifier_physical_defense: int
    _modifier_special_defense: int

    def __post_init__(self):
        if self._base_physical_defense <=0:
            emsg = "BASE-PHYSICAL-DEFENSE must be positive"
            logger.error(emsg)
            raise ValueError(emsg)

        if self._base_special_defense <=0:
            emsg = "BASE-SPECIAL-DEFENSE must be positive"
            logger.error(emsg)
            raise ValueError(emsg)


    #getter and setters :
    @property
    def base_physical_defense(self)->int:
        return self._base_physical_defense

    @base_physical_defense.setter
    def base_physical_defense(self,base_physical_defense:int)->None:
        if not isinstance(base_physical_defense,int):
            emsg = "BASE-PHYSICAL-DEFENSE must be an 'int' type"
            logger.error(emsg)
            raise TypeError(emsg)
        self._base_physical_defense = base_physical_defense
        return

    @property
    def base_special_defense(self)->int:
        return self._base_special_defense

    @base_special_defense.setter
    def base_special_defense(self,base_special_defense)->None:
        if not isinstance(base_special_defense,int):
            emsg = "BASE-SPECIAL-DEFENSE must be an 'int' type"
            logger.error(emsg)
            raise TypeError(emsg)
        self._base_physical_defense = base_special_defense
        return

    @property
    def modifier_physical_defense(self)->int:
        return self._modifier_physical_defense

    @modifier_physical_defense.setter
    def modifier_physical_defense(self,modifier_physical_defense)->None:
        if not isinstance(modifier_physical_defense,int):
            emsg = "MODIFIER-PHYSICAL-DEFENSE must be an 'int' type"
            logger.error(emsg)
            raise TypeError(emsg)
        self._base_physical_defense = modifier_physical_defense
        return

    @property
    def modifier_special_defense(self)->int:
        return self._modifier_special_defense

    @modifier_special_defense.setter
    def modifier_special_defense(self,modifier_special_defense)->None:
        if not isinstance(modifier_special_defense,int):
            emsg = "MODIFIER-SPECIAL-DEFENSE must be an 'int' type"
            logger.error(emsg)
            raise TypeError(emsg)
        self._base_physical_defense = modifier_special_defense
        return

    @property
    def current_physical_defense(self)->int:
        return self._base_physical_defense + self._modifier_physical_defense

    @property
    def current_special_defense(self)->int:
        return self._base_special_defense + self._modifier_special_defense
    

    


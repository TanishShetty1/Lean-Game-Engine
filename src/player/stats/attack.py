import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Attack:
    _base_physical_attack : int
    _modifier_physical_attack : int
    _base_special_attack : int
    _modifier_special_attack : int

    def __post_init__(self):
        if self._base_physical_attack < 0:
            emsg = "BASE-PHYSICAL-ATTACK must be non-negative"
            logger.error(emsg)
            raise ValueError(emsg)

        if self._base_special_attack < 0:
            emsg = "BASE-SPECIAL-ATTACK must be non-negative"
            logger.error(emsg)
            raise ValueError(emsg)


    #getters and setters :
    @property
    def base_physical_attack(self)->int:
        return self._base_physical_attack

    @base_physical_attack.setter
    def base_physical_attack(self,base_physical_attack)->None:
        if not isinstance(base_physical_attack,int):
            emsg = "BASE-PHYSICAL-ATTACK must be an 'int' type"
            logger.error(emsg)
            raise TypeError(emsg)
        self._base_physical_attack = base_physical_attack

    @property
    def base_special_attack(self)->int:
        return self._base_special_attack

    @base_special_attack.setter
    def base_special_attack(self,base_special_attack)->None:
        if not isinstance(base_special_attack,int):
            emsg = "BASE-SPECIAL-ATTACK must be an 'int' type"
            logger.error(emsg)
            raise TypeError(emsg)
        self._base_special_attack = base_special_attack

    @property
    def modifier_physical_attack(self)->int:
        return self._modifier_physical_attack

    @modifier_physical_attack.setter
    def modifier_physical_attack(self,modifier_physical_attack)->None:
        if not isinstance(modifier_physical_attack,int):
            emsg = "MODIFIER-PHYSICAL-ATTACK must be an 'int' type"
            logger.error(emsg)
            raise TypeError(emsg)
        self._modifier_physical_attack = modifier_physical_attack

    @property
    def modifier_special_attack(self)->int:
        return self._modifier_special_attack

    @modifier_special_attack.setter
    def modifier_special_attack(self,modifier_special_attack)->None:
        if not isinstance(modifier_special_attack,int):
            emsg = "MODIFIER-SPECIAL-ATTACK must be an 'int' type"
            logger.error(emsg)
            raise TypeError(emsg)
        self._modifier_special_attack = modifier_special_attack

    @property
    def current_physical_attack(self)->int:
        return self._base_physical_attack + self._modifier_physical_attack

    @property
    def current_special_attack(self)->int:
        return self._base_special_attack + self._modifier_special_attack
    

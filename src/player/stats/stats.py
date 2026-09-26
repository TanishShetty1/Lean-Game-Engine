import logging

from dataclasses import dataclass
from health import Health

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Stats:
    _health : Health

    @property 
    def health(self)->Health:
        return self._health

    @health.setter
    def health(self,health:Health)->None:
        if not isinstance(health,Health):
            emsg = f"{health} must be an 'Health' instance"
            logger.warning(emsg)
            raise TypeError(emsg)
        self._health = health
import logging
from enums import Resource, Terrain

logger = logging.getLogger(__name__)

class Tile:

    def __init__(self) -> None:
        self._resource = Resource.DEFAULT
        self._terrain = Terrain.DEFAULT
        self._occupied = False

    def occupy_tile(self)->bool:
        if self._occupied:
            logger.info("Tile is already occupied")
            return False
        
        self._occupied = True
        return True

    def exit_tile(self)->None:
        self._occupied = False

    def get_resource(self)->Resource:
        return self._resource

    def get_terrain(self)->Terrain:
        return self._terrain

    def is_occupied(self)->bool:
        return self._occupied

    def _set_terrain(self,terrain:Terrain)->bool:
        if not isinstance(terrain,Terrain):
            msg = f"{terrain} is not a valid Terrain type"
            logger.warning(msg)
            return False

        self._terrain = terrain
        return True

    def _set_resource(self,resource:Resource)->bool:
        if not isinstance(resource,Resource):
            msg = f"{resource} is not a valid Resource type"
            logger.warning(msg)
            return False
        
        self._resource = resource
        return True


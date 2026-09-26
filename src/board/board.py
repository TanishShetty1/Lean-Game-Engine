from tile import Tile

class Board:

    def __init__(self,rows:int,columns:int)->None:
        self._rows = rows
        self._columns = columns
        self._grid = [[Tile() for _ in range(columns)] for _ in range(rows)]
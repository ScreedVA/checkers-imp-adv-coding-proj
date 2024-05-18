from typing import List, Tuple

class CheckerStatus:
    def __init__(self, pos) -> None:
        self.__pos: List[Tuple] = pos
        self.options: List = []

    def get_pos(self):
        return self.__pos
    



from typing import List, Tuple

class CheckerStatus:
    def __init__(self, pos, types) -> None:
        self.pos: List[Tuple] = pos
        self.all_pieces: List[str] = types
        # self.options: List = []
        
        self.capt_types: List[str] = []
        self.capt_pos: List[Tuple] = []

    def get_pos(self):
        return self.pos
    
    
    



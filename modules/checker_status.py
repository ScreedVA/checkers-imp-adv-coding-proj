from typing import List, Tuple

class CheckerStatus:
    def __init__(self, pos) -> None:
        self.pos: List[Tuple] = pos
        self.all_pieces: List[str] = ["man"] * 12
        # self.options: List = []
        
        self.captured_pieces_types: List[str] = []
        self.captured_pieces_pos: List[Tuple] = []

    def get_pos(self):
        return self.pos
    
    
    



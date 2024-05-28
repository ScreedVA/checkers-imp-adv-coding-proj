from typing import List, Tuple

class CheckerStatus:
    def __init__(self, pos, types, capt_pos, capt_types) -> None:
        self.pos: List[Tuple] = self.convert_to_int(pos)
        self.types: List[str] = types
        # self.options: List = []
        
        self.capt_pos: List[Tuple] = capt_pos
        self.capt_types: List[str] = capt_types

    def convert_to_int(self, l_t):
        return [(int(x),int(y)) for x , y in l_t]


    def get_pos(self):
        return self.pos
    
    
    



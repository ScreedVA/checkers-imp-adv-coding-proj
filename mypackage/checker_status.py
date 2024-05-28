from typing import List, Tuple

class CheckerStatus:
    """Class to handle and record changes in the white and black checker objects"""
    def __init__(self, pos, types, capt_pos, capt_types) -> None:
        """Initilizes checker position, type and captures"""
        self.pos: List[Tuple] = self.convert_to_int(pos)
        self.types: List[str] = types
        
        self.capt_pos: List[Tuple] = capt_pos
        self.capt_types: List[str] = capt_types

    def convert_to_int(self, l_t):
        """Will convert possible float coordinates into integers upon initialization"""
        return [(int(x),int(y)) for x , y in l_t]


    def get_pos(self):
        """Getter which returns checker positions"""
        return self.pos
    
    
    



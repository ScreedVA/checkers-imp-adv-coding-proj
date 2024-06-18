from PIL import Image
from pygame import image, transform, Surface
from typing import Tuple, List



class ImageHandler:
    """Class for handling game image loading and cropping"""
    def __init__(self):
        self.checkers_img = Image.open("static/images/checkers.png")
        self._size : Tuple[int]
        self._size_small: Tuple[int]

    def get_black_checker(self, size="normal") -> Surface:
        """Retuns a black checker image as a pygame surface"""
        if size == "small":
            return transform.scale(self.pil_to_surface(self.checkers_img.crop((64, 0, 96, 32))), self._size_small)
        return transform.scale(self.pil_to_surface(self.checkers_img.crop((64, 0, 96, 32))), self._size)
    
    def get_white_checker(self, size="normal") -> Surface:
        """Retuns a white checker image as a pygame surface"""
        if size == "small":
            return transform.scale(self.pil_to_surface(self.checkers_img.crop((96, 0, 128, 32))), self._size_small)
        return transform.scale(self.pil_to_surface(self.checkers_img.crop((96, 0, 128, 32))), self._size)
    
    def get_black_king(self, size="normal") -> Surface:
        """Retuns a black king image as a pygame surface"""
        if size == "small":
            return transform.scale(self.pil_to_surface(self.checkers_img.crop((0, 0, 32, 32))), self._size_small)
        return transform.scale(self.pil_to_surface(self.checkers_img.crop((0, 0, 32, 32))), self._size)
    
    def get_white_king(self, size="normal") -> Surface:
        """Retuns a white king image as a pygame surface"""
        if size == "small":
            return transform.scale(self.pil_to_surface(self.checkers_img.crop((32, 0, 64, 32))), self._size_small)
        return transform.scale(self.pil_to_surface(self.checkers_img.crop((32, 0, 64, 32))), self._size)
    
    def pil_to_surface(self, pil_image) -> Surface:
        """Convert a PILLOW image to a Pygame surface."""
        mode = pil_image.mode
        size = pil_image.size
        data = pil_image.tobytes()
        # print(f"Mode :{mode}")
        # print(f"Size :{size}")
        # print(f"Data :{data}")
        # Create a surface from the string data
        surface = image.fromstring(data, size, mode)
        return surface

class ManHandler:
     
     def _eval_men(self, cord: Tuple[int | float]) -> List[Tuple[int | float]]:
        """Checks and validates all possible moves for a given man piece"""
        possible_positions: List[Tuple[int | float]] = []
        if self._current_player == "p1":
                # Initiliaze possible positions
                r_d = (cord[0] + 1, cord[1] + 1)
                l_d = (cord[0] - 1, cord[1] + 1)
                r_d_2x = (cord[0] + 2, cord[1] + 2)
                l_d_2x = (cord[0] - 2, cord[1] + 2)
                if 0 <= cord[0] <= 7 and cord[1] <= 7:
                    # Check if position at 1 right and 1 down is valid
                    if (r_d not in self._player_2_cords) and (r_d not in self._player_1_cords) and (0 <= cord[0] + 1 <= 7) and (0 <= cord[1] + 1 <= 7):
                        possible_positions.append(r_d)
                    # Check if position at 1 left and 1 down is valid
                    if (l_d not in self._player_2_cords) and (l_d not in self._player_1_cords) and (0 <= cord[0] - 1 <= 7) and (0 <= cord[1] + 1 <= 7):
                         possible_positions.append(l_d)
                    # Check if position at 2 right and 2 down is valid
                    if (r_d_2x not in self._player_1_cords) and (r_d_2x not in self._player_2_cords) and (r_d not in self._player_1_cords) and (0 <= cord[0] + 2 <= 7) and (0 <= cord[1] + 2 <= 7) and (r_d in self._player_2_cords):
                         possible_positions.append(r_d_2x)
                    # Check if position at 2 left and 2 down is valid
                    if (l_d_2x not in self._player_1_cords) and  (l_d_2x not in self._player_2_cords) and (l_d not in self._player_1_cords) and (0 <= cord[0] - 2 <= 7) and (0 <= cord[1] + 2 <= 7) and (l_d in self._player_2_cords):
                        possible_positions.append(l_d_2x)
        
        
        if self._current_player == "p2":
                # Initiliaze possible positions
                r_t = (cord[0] + 1, cord[1] - 1)
                l_t = (cord[0] - 1, cord[1] - 1)
                r_t_2x = (cord[0] + 2, cord[1] - 2)
                l_t_2x = (cord[0] - 2, cord[1] - 2)
                if cord[0] <= 7 and cord[0] >= 0 and (cord[1] <= 7):
                    # Check if position at 1 right and 1 up is valid
                    if (r_t not in self._player_2_cords) and (r_t not in self._player_1_cords) and (0 <= (cord[0] + 1) <= 7):
                        possible_positions.append(r_t)
                    # Check if position at 1 left and 1 up is valid
                    if (l_t not in self._player_2_cords) and (l_t not in self._player_1_cords) and (0 <= (cord[0] - 1) <= 7):
                            possible_positions.append(l_t)
                    # Check if position at 2 right and 2 up is valid
                    if (r_t_2x not in self._player_2_cords) and  (r_t_2x not in self._player_1_cords) and (r_t not in self._player_2_cords) and (0 <= cord[0] + 2 <= 7) and (r_t in self._player_1_cords):
                            possible_positions.append(r_t_2x)
                    # Check if position at 2 left and 2 up is valid
                    if (l_t_2x not in self._player_2_cords) and (l_t_2x not in self._player_1_cords) and (l_t not in self._player_2_cords) and (0 <= cord[0] - 2 <= 7) and (l_t in self._player_1_cords):
                        possible_positions.append(l_t_2x)
        return possible_positions
    

class KingHandler(ManHandler):
    def __init__(self) -> None:
         super().__init__()
     
    def _eval_king(self, cord):
        """Checks and validates all possible moves for a given king piece"""
        possible_positions = self._eval_men(cord)
        
        if self._current_player == "p1":
                # Initiliaze possible positions
                r_t = (cord[0] + 1, cord[1] - 1)
                l_t = (cord[0] - 1, cord[1] - 1)
                r_t_2x = (cord[0] + 2, cord[1] - 2)
                l_t_2x = (cord[0] - 2, cord[1] - 2)
                if (cord[0] <= 7) and (cord[0] >= 0) and (cord[1] <= 7):
                    # Check if position at 1 right and 1 up is valid
                    if (r_t not in self._player_2_cords) and (r_t not in self._player_1_cords) and (0 <= (cord[0] + 1) <= 7):
                        possible_positions.append(r_t)
                    # Check if position at 1 left and 1 up is valid
                    if (l_t not in self._player_2_cords) and (l_t not in self._player_1_cords) and (0 <= (cord[0] - 1) <= 7):
                            possible_positions.append(l_t)
                    # Check if position at 2 right and 2 up is valid
                    if (r_t_2x not in self._player_2_cords) and  (r_t_2x not in self._player_1_cords) and (r_t not in self._player_1_cords) and (0 <= cord[0] + 2 <= 7) and (r_t in self._player_2_cords):
                            possible_positions.append(r_t_2x)
                    # Check if position at 2 left and 2 up is valid
                    if (l_t_2x not in self._player_2_cords) and (l_t_2x not in self._player_1_cords) and (l_t not in self._player_1_cords) and (0 <= cord[0] - 2 <= 7) and (l_t in self._player_2_cords):
                        possible_positions.append(l_t_2x)

        if self._current_player == "p2":
                # Initiliaze possible positions
                r_d = (cord[0] + 1, cord[1] + 1)
                l_d = (cord[0] - 1, cord[1] + 1)
                r_d_2x = (cord[0] + 2, cord[1] + 2)
                l_d_2x = (cord[0] - 2, cord[1] + 2)
                if (0 <= cord[0] <= 7) and (cord[1] <= 7):
                    # Check if position at 1 right and 1 down is valid
                    if r_d not in self._player_2_cords and r_d not in self._player_1_cords and 0 <= cord[0] + 1 <= 7:
                        possible_positions.append(r_d)
                    # Check if position at 1 left and 1 down is valid
                    if l_d not in self._player_2_cords and l_d not in self._player_1_cords and 0 <= cord[0] - 1 <= 7:
                         possible_positions.append(l_d)
                    # Check if position at 2 right and 2 down is valid
                    if r_d_2x not in self._player_1_cords and r_d_2x not in self._player_2_cords and r_d not in self._player_2_cords and 0 <= cord[0] + 2 <= 7 and r_d in self._player_1_cords:
                         possible_positions.append(r_d_2x)
                    # Check if position at 2 left and 2 down is valid
                    if l_d_2x not in self._player_1_cords and  l_d_2x not in self._player_2_cords and l_d not in self._player_2_cords and 0 <= cord[0] - 2 <= 7 and l_d in self._player_1_cords:
                        possible_positions.append(l_d_2x)
        return possible_positions


    
        


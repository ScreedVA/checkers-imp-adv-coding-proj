from PIL import Image
from pygame import image, transform, Surface
from typing import Tuple



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
    

    

    
        


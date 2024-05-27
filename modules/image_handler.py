from PIL import Image
from pygame import image, transform

class ImageHandler:
    def __init__(self, size=(100,100), size_small=(50,50)):
        self.checkers_img = Image.open("static/images/checkers.png")
        self.__size = size
        self.__size_small = size_small

    def get_black_checker(self, size="normal"):
        if size == "small":
            return transform.scale(self.pil_to_surface(self.checkers_img.crop((64, 0, 96, 32))), self.__size_small)
        return transform.scale(self.pil_to_surface(self.checkers_img.crop((64, 0, 96, 32))), self.__size)
    
    def get_white_checker(self, size="normal"):
        if size == "small":
            return transform.scale(self.pil_to_surface(self.checkers_img.crop((96, 0, 128, 32))), self.__size_small)
        return transform.scale(self.pil_to_surface(self.checkers_img.crop((96, 0, 128, 32))), self.__size)
    
    def get_black_king(self, size="normal"):
        if size == "small":
            return transform.scale(self.pil_to_surface(self.checkers_img.crop((0, 0, 32, 32))), self.__size)
        return transform.scale(self.pil_to_surface(self.checkers_img.crop((0, 0, 32, 32))), self.__size)
    
    def get_white_king(self, size="normal"):
        if size == "small":
            return transform.scale(self.pil_to_surface(self.checkers_img.crop((32, 0, 64, 32))), self.__size)
        return transform.scale(self.pil_to_surface(self.checkers_img.crop((32, 0, 64, 32))), self.__size)
    
    def pil_to_surface(self, pil_image):
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
    

    

    
        


from pygame import draw, Rect

class GameBoard:
    def __init__(self, black_checkers, white_checkers, diff=1) -> None:
        """Initializes default board settings"""
        self.__width = 1000 * diff
        self.__height = 1000 * diff
        self.__colors = {"bg": "#ffe4ba", 
                         "square": "#e3ae5c",
                         "border": "black"}
        self.__bc = black_checkers
        self.__wc = white_checkers

    def post_init(self, image_handler, game_controls):
        self.__img_h = image_handler
        self.__gc = game_controls
    

    def get_board_size(self):
        return (self.__width, self.__height)
        
    def get_bg_color(self):
        return self.__colors["bg"]
    
    def get_square_color(self):
        return self.__colors["square"]

    def get_border_color(self):
        return self.__colors["border"]

    def get_square_space(self):
        return (self.get_square_size(), self.get_square_size())
    
    def get_square_size(self):
        return (self.__width // 10)

    
    def render_board(self, surface): 
        surface.fill(self.get_bg_color())
        for i in range(32):
            row = i // 4
            column = i % 4
            diff = column * (self.get_square_size() * 2) # diff = (0 -> 200 -> 400 -> 600)
            if row % 2 == 0:
                """Draw gray square when row = (0 -> 2 -> 4 -> 6)"""
                draw.rect(surface, self.get_square_color(), [((self.__width * 0.6 - diff), (row * self.get_square_size())), self.get_square_space()])
            else:
                """Draw gray square when row =(1 -> 3 -> 5 -> 7)"""
                draw.rect(surface, self.get_square_color(), [((self.__width * 0.7 - diff), (row * self.get_square_size())), self.get_square_space()])
        for i in range(9):
            """Draw horizontal border lines"""
            draw.line(surface, self.get_border_color(), (0, i * self.get_square_size()), (self.__width * 0.8, i * self.get_square_size()))
            """Draw vertical border lines"""
            draw.line(surface, self.get_border_color(), (i * self.get_square_size(), 0), (i * self.get_square_size(), self.__height * 0.8))
        """Draw border for game status view """
        draw.rect(surface, self.get_border_color(), [(0, self.__height * 0.8),(self.__width * 0.8, self.__height * 0.2 )], 3)
        """Draw border for captured men view"""
        draw.rect(surface, self.get_border_color(), [(self.__width * 0.8, 0),(self.__width * 0.2, self.__height * 0.8)], 3)
        self.render_pieces(surface)
        """Update selection displayed"""

    def render_pieces(self, surface):
        """Render each pice onto the board when called"""
        for pos in self.__bc.get_pos():
            surface.blit(self.__img_h.get_black_checker(), (pos[0] * self.get_square_size(), pos[1] * self.get_square_size()))
        for pos in self.__wc.get_pos():
            surface.blit(self.__img_h.get_white_checker(), (pos[0] * self.get_square_size(), pos[1] * self.get_square_size()))




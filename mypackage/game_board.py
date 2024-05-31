from pygame import draw, font
font.init()



class GameBoardDef:
    def __init__(self, b_c, w_c, w, h, diff=1) -> None:
        """Initiliazs default game board settings"""
        self._width = w * diff
        self._height = h * diff
        self._colors = {"bg": "#ffe4ba",
                         "square": "#e3ae5c",
                         "border": "black"}
        self._bc = b_c
        self._wc = w_c
class GameBoard(GameBoardDef):
    """Class to handle game board functionality"""
    def __init__(self, b_c, w_c, w, h, diff=1) -> None:
        super().__init__(b_c, w_c, w, h, diff)
        self.font_init()

    def post_init(self, image_handler, game_controls):
        self.__img_h = image_handler
        self.__gc = game_controls
    
    def font_init(self):
        self.gs_font = font.Font("static/fonts/DaniloCatalina.ttf", int(self.get_square_size() * 0.8))
        self.w_font = font.Font("static/fonts/DaniloCatalina.ttf", int(self.get_square_size() * 0.8))

    def get_board_size(self):
        """Getter which returns size of game board"""
        return (self._width, self._height)
        
    def get_bg_color(self):
        """Getter which returns background color from colors dictionary"""
        return self._colors["bg"]
    
    def get_square_color(self):
        """Getter which returns the square color from colors dictionary"""
        return self._colors["square"]

    def get_border_color(self):
        """Getter which returns the border color from colors dictionary"""
        return self._colors["border"]

    def get_square_space(self):
        """Getter which returns the width and height of the board squares in a tuple"""
        return (self.get_square_size(), self.get_square_size())
    
    def get_square_size(self):
        """Getter which returns the width of the board squares"""
        return (self._width // 10)

    
    def render_board(self, surface): 
        """Renders 32 squares squares, 9 vertical and 9 horizontal lines onto the screen
        (excecutes render_pieces(), render_game_status() and render_captures() functions)"""
        surface.fill(self.get_bg_color())
        for i in range(32):
            y = i // 4
            x = i % 4
            diff = x * (self.get_square_size() * 2) # diff = (0 -> 200 -> 400 -> 600)
            if y % 2 == 0:
                """Draw gray square when y = (0 -> 2 -> 4 -> 6)"""
                draw.rect(surface, self.get_square_color(), [((self._width * 0.6 - diff), (y * self.get_square_size())), self.get_square_space()])
            else:
                """Draw gray square when y =(1 -> 3 -> 5 -> 7)"""
                draw.rect(surface, self.get_square_color(), [((self._width * 0.7 - diff), (y * self.get_square_size())), self.get_square_space()])
        for i in range(9):
            """Draw horizontal border lines"""
            draw.line(surface, self.get_border_color(), (0, i * self.get_square_size()), (self._width * 0.8, i * self.get_square_size()))
            """Draw vertical border lines"""
            draw.line(surface, self.get_border_color(), (i * self.get_square_size(), 0), (i * self.get_square_size(), self._height * 0.8))
        """Draw border for game status view """
        draw.rect(surface, self.get_border_color(), [(0, self._height * 0.8),(self._width * 0.8, self._height * 0.2 )], 3)
        """Draw border for captured men view"""
        draw.rect(surface, self.get_border_color(), [(self._width * 0.8, 0),(self._width * 0.2, self._height * 0.8)], 3)
        
        self.render_pieces(surface)

        self.render_game_status(surface)

        self.render_captured(surface)

    def render_pieces(self, surface):
        """Renders each piece in CheckStatus.pos object lists onto the board when called"""
        for i in range(len(self._bc.get_pos())):
            # Check if black piece is a man
            if self._bc.types[i] == "man":
                surface.blit(self.__img_h.get_black_checker(), (self._bc.get_pos()[i][0] * self.get_square_size(), self._bc.get_pos()[i][1] * self.get_square_size()))
            # Check if black piece is a king
            elif self._bc.types[i] == "king":
                surface.blit(self.__img_h.get_black_king(), (self._bc.get_pos()[i][0] * self.get_square_size(), self._bc.get_pos()[i][1] * self.get_square_size()))

        for i in range(len(self._wc.get_pos())):
            # Check if white piece is a man 
            if self._wc.types[i] == "man":
                surface.blit(self.__img_h.get_white_checker(), (self._wc.get_pos()[i][0] * self.get_square_size(), self._wc.get_pos()[i][1] * self.get_square_size()))
        # Check if white piece is a king
            elif self._wc.types[i] == "king":
                surface.blit(self.__img_h.get_white_king(), (self._wc.get_pos()[i][0] * self.get_square_size(), self._wc.get_pos()[i][1] * self.get_square_size()))


    def render_game_status(self, surface):
        """Render the game message prompts to players"""
        dest = (self.get_square_size() * 0.1, self._height * 0.85)
        if self.__gc.lch["p2"]["moved"]:
            surface.blit(self.gs_font.render("Black select a Piece", True, "black"), dest)
        if self.__gc.lch["p1"]["selected"]:
            surface.blit(self.gs_font.render("Black move a Piece", True, "black"), dest)
        if self.__gc.lch["p1"]["moved"]:
            surface.blit(self.gs_font.render("White select a Piece", True, "black"), dest)
        if self.__gc.lch["p2"]["selected"]:
            surface.blit(self.gs_font.render("White move a Piece", True, "black"), dest)

    def render_captured(self, surface):
        """Renders all captured pieces at the right side of the screen"""
        for i in range(len(self._bc.capt_types)):
            # Check if white piece is a man or king
            if self._bc.capt_types[i] == "man":
                surface.blit(self.__img_h.get_white_checker("small"), (self._width * 0.8, i * self.get_square_size() // 2))
            elif self._bc.capt_types[i] == "king":
                surface.blit(self.__img_h.get_white_king("small"), (self._width * 0.8, i * self.get_square_size() // 2))
        
        for i in range(len(self._wc.capt_types)):
            # Check if black piece is a man or king
            if self._wc.capt_types[i] == "man":
                surface.blit(self.__img_h.get_black_checker("small"), (self._width * 0.9, i * self.get_square_size() // 2))
            elif self._wc.capt_types[i] == "king":
                surface.blit(self.__img_h.get_black_king("small"), (self._width * 0.9, i * self.get_square_size() // 2))
        
    def render_winner(self, surface):
        """Renders winning text when life cycle hook detects a winner"""
        dest = (self._width * 0.05, self._height * 0.3)
        if self.__gc.lch["winner"] == "black(p1)":
            surface.blit(self.w_font.render("Black(P1) is the Winner", True, "black"), dest)
        elif self.__gc.lch["winner"] == "white(p2)":
            surface.blit(self.w_font.render("White(P2) is the Winner", True, "black"), dest)




        
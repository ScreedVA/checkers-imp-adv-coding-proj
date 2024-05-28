from pygame import draw, Rect, font
font.init()
class GameBoard:
    def __init__(self, black_checkers, white_checkers, width, height, diff=1) -> None:
        """Initializes default board settings"""
        self.__width = width * diff
        self.__height = height * diff
        self.__colors = {"bg": "#ffe4ba", 
                         "square": "#e3ae5c",
                         "border": "black"}
        self.__bc = black_checkers
        self.__wc = white_checkers
        self.gs_font = font.Font("static/fonts/DaniloCatalina.ttf", int(self.get_square_size() * 0.8))
        self.w_font = font.Font("static/fonts/DaniloCatalina.ttf", int(self.get_square_size() * 0.8))

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

        self.render_game_status(surface)

        self.render_captured(surface)

    def render_pieces(self, surface):
        """Render each pice onto the board when called"""
        for i in range(len(self.__bc.get_pos())):
            # Check if black piece is a man
            if self.__bc.types[i] == "man":
                surface.blit(self.__img_h.get_black_checker(), (self.__bc.get_pos()[i][0] * self.get_square_size(), self.__bc.get_pos()[i][1] * self.get_square_size()))
            # Check if black piece is a king
            elif self.__bc.types[i] == "king":
                surface.blit(self.__img_h.get_black_king(), (self.__bc.get_pos()[i][0] * self.get_square_size(), self.__bc.get_pos()[i][1] * self.get_square_size()))

        for i in range(len(self.__wc.get_pos())):
            # Check if white piece is a man 
            if self.__wc.types[i] == "man":
                surface.blit(self.__img_h.get_white_checker(), (self.__wc.get_pos()[i][0] * self.get_square_size(), self.__wc.get_pos()[i][1] * self.get_square_size()))
        # Check if white piece is a king
            elif self.__wc.types[i] == "king":
                surface.blit(self.__img_h.get_white_king(), (self.__wc.get_pos()[i][0] * self.get_square_size(), self.__wc.get_pos()[i][1] * self.get_square_size()))


    def render_game_status(self, surface):
        """Render the game message prompts to players"""
        dest = (self.get_square_size() * 0.1, self.__height * 0.85)
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
        for i in range(len(self.__bc.capt_types)):
            # Check if white piece is a man or king
            if self.__bc.capt_types[i] == "man":
                surface.blit(self.__img_h.get_white_checker("small"), (self.__width * 0.8, i * self.get_square_size() // 2))
            elif self.__bc.capt_types[i] == "king":
                surface.blit(self.__img_h.get_white_king("small"), (self.__width * 0.8, i * self.get_square_size() // 2))
        
        for i in range(len(self.__wc.capt_types)):
            # Check if black piece is a man or king
            if self.__wc.capt_types[i] == "man":
                surface.blit(self.__img_h.get_black_checker("small"), (self.__width * 0.9, i * self.get_square_size() // 2))
            elif self.__wc.capt_types[i] == "king":
                surface.blit(self.__img_h.get_black_king("small"), (self.__width * 0.9, i * self.get_square_size() // 2))
        
    def render_winner(self, surface):
        dest = (self.__width * 0.05, self.__height * 0.3)
        if self.__gc.lch["winner"] == "black(p1)":
            surface.blit(self.w_font.render("Black(P1) is the Winner", True, "black"), dest)
        elif self.__gc.lch["winner"] == "white(p2)":
            surface.blit(self.w_font.render("White(P2) is the Winner", True, "black"), dest)
        
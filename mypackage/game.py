from pygame import draw, font
from typing import List, Tuple
import json
import time
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

class GameRecord:
    """Class which handles json game data"""
    def __init__(self) -> None:
        """Initiliazes GameRecord variables"""
        self.file_path = "game_record.json"
    

    def update_record(self,b_c, w_c):
        """Will update the game record json file with the most recent game data"""
        data = {
            "pos": {
                "black_pos": b_c.pos,
                "white_pos": w_c.pos
            },
            "types": {
                "black_types": b_c.types,
                "white_types": w_c.types
            },
            "capt_pos": {
                "b_capt_pos": b_c.capt_pos,
                "w_capt_pos": w_c.capt_pos
            },
            "capt_types": {
                "b_capt_types": b_c.capt_types,
                "w_capt_types": w_c.capt_types
            }
            
        }
        with open("game_record.json", "w") as f:
            json.dump(data, f,  indent=1)

    def _read_record(self):
        """Returns previous game data or none"""
        try:
            with open("game_record.json", "r") as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            # print(f"The file '{self.file_path}' was not found")
            return None
        
    def _check_record(self):
        """Returns true if previous game data exists"""
        if self._read_record():
            return True
        return False
    
class GameInterface(GameRecord):
    def __init__(self, start) -> None:
        self.__start = start


    def configure_game(self):
        # Checks if user has a previously saved game
        if self._check_record():
            new_or_load = input("\nWould you like to load(L) your previous game or start a new game(N)\n").title()
            if new_or_load == "L":
                data = self._read_record()
                print("\nLoading previous round...")
                self.__start(data["pos"]["black_pos"], 
                    data["pos"]["white_pos"], 
                    data["types"]["black_types"], 
                    data["types"]["white_types"],
                    data["capt_pos"]["b_capt_pos"],
                    data["capt_pos"]["w_capt_pos"],
                    data["capt_types"]["b_capt_types"],
                    data["capt_types"]["w_capt_types"],
                    )
                
            elif new_or_load == "N":
                print("\nStarting new round...")
                self.__start()
            else:
                print(f"'{new_or_load}' is an invalid input, enter either L or N\n")
                time.sleep(1)
        else:
            print("You have no previous games, Starting round...")
            self.__start()

class GameCheckerStatus:
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

class GameControls:
    """Class to control game logic, turn handling and behaviour"""
    def __init__(self,  sqaure_space, black_checkers, white_checkers) -> None:
        """Initiliazes default game control settings"""
        self.__square_space = sqaure_space
        self.__colors = {"p1": "#d70000", "p2": "#0229bf", "indicator":"#2db83d"}
        self.__current_player = "p1"
        self.__players = {"p1": black_checkers, "p2": white_checkers}
        self.__player_1_cords = self.__players["p1"].get_pos()
        self.__player_2_cords = self.__players["p2"].get_pos()
        self.__player_1_types = self.__players["p1"].types
        self.__player_2_types = self.__players["p2"].types
        self.lch = {"p1": {"selected": False,"moved": False}, "p2": {"selected": False, "moved": True}, "winner": None}
        self.select_cord = None
        self.current_player_cords = self.__players[self.__current_player].get_pos()
        self.font = font.Font("static/fonts/DaniloCatalina.ttf", )


    def render_selection(self,surface):
        if self.select_cord:
                """Check if player has selected a black(p1) piece when black is the current player"""
                if self.__current_player == "p1":
                    if self.select_cord in self.__player_1_cords:
                        self.__render_valid_options(surface)
                        pos = (self.select_cord[0] * self.__square_space[0], self.select_cord[1] * self.__square_space[0])
                        draw.rect(surface, self.__colors[self.__current_player], [pos, self.__square_space], 3)
                
                """Check if player has selected a white(p2) piece when white is the current player"""
                if self.__current_player == "p2":
                    if self.select_cord in self.__player_2_cords:
                        self.__render_valid_options(surface)
                        pos = (self.select_cord[0] * self.__square_space[0], self.select_cord[1] * self.__square_space[0])
                        draw.rect(surface, self.__colors[self.__current_player], [pos, self.__square_space], 3)

    def set_current_player(self, player):
         """Setter for current player"""
         self.__current_player = player

    def get_current_player(self):
        """Getter for current player"""
        return self.__current_player


    def check_options(self):
        """Checks for all the possible moves for each piece of the current player"""
        all_moves = []
        moves_list = []
        if self.__current_player == "p1":
            for i in range(len(self.__player_1_cords)):
                # Check if black player(p1) piece is a man
                if self.__player_1_types[i] == "man":
                    moves_list = self.__check_men(self.__player_1_cords[i])
                    all_moves.append(moves_list)
                # check if black player(p1) piece is a king
                elif self.__player_1_types[i] == "king":
                    moves_list = self.__check_king(self.__player_1_cords[i])
                    all_moves.append(moves_list)


        elif self.__current_player == "p2":
            for i  in range(len(self.__player_2_cords)):
                # Check if white player(p2) piece is a man
                if self.__player_2_types[i] == "man":
                    moves_list = self.__check_men(self.__player_2_cords[i])
                    all_moves.append(moves_list)
                # Check if white player(p2) piece is a king
                elif self.__player_2_types[i] == "king":
                    moves_list = self.__check_king(self.__player_2_cords[i])
                    all_moves.append(moves_list)
                     
            
        return all_moves
    
    def __check_men(self, cord):
        """Checks and validates all possible moves for a given man piece"""
        moves_list = []
        if self.__current_player == "p1":
                r_d = (cord[0] + 1, cord[1] + 1)
                l_d = (cord[0] - 1, cord[1] + 1)
                r_d_2x = (cord[0] + 2, cord[1] + 2)
                l_d_2x = (cord[0] - 2, cord[1] + 2)
                if 0 <= cord[0] <= 7 and cord[1] <= 7:
                    # Check if position at 1 right and 1 down is valid
                    if (r_d not in self.__player_2_cords) and (r_d not in self.__player_1_cords) and (0 <= cord[0] + 1 <= 7) and (0 <= cord[1] + 1 <= 7):
                        moves_list.append(r_d)
                    # Check if position at 1 left and 1 down is valid
                    if (l_d not in self.__player_2_cords) and (l_d not in self.__player_1_cords) and (0 <= cord[0] - 1 <= 7) and (0 <= cord[1] + 1 <= 7):
                         moves_list.append(l_d)
                    # Check if position at 2 right and 2 down is valid
                    if (r_d_2x not in self.__player_1_cords) and (r_d_2x not in self.__player_2_cords) and (r_d not in self.__player_1_cords) and (0 <= cord[0] + 2 <= 7) and (0 <= cord[1] + 2 <= 7) and (r_d in self.__player_2_cords):
                         moves_list.append(r_d_2x)
                    # Check if position at 2 left and 2 down is valid
                    if (l_d_2x not in self.__player_1_cords) and  (l_d_2x not in self.__player_2_cords) and (l_d not in self.__player_1_cords) and (0 <= cord[0] - 2 <= 7) and (0 <= cord[1] + 2 <= 7) and (l_d in self.__player_2_cords):
                        moves_list.append(l_d_2x)
        
        
        if self.__current_player == "p2":
                r_t = (cord[0] + 1, cord[1] - 1)
                l_t = (cord[0] - 1, cord[1] - 1)
                r_t_2x = (cord[0] + 2, cord[1] - 2)
                l_t_2x = (cord[0] - 2, cord[1] - 2)
                if cord[0] <= 7 and cord[0] >= 0 and (cord[1] <= 7):
                    # Check if position at 1 right and 1 up is valid
                    if (r_t not in self.__player_2_cords) and (r_t not in self.__player_1_cords) and (0 <= (cord[0] + 1) <= 7):
                        moves_list.append(r_t)
                    # Check if position at 1 left and 1 up is valid
                    if (l_t not in self.__player_2_cords) and (l_t not in self.__player_1_cords) and (0 <= (cord[0] - 1) <= 7):
                            moves_list.append(l_t)
                    # Check if position at 2 right and 2 up is valid
                    if (r_t_2x not in self.__player_2_cords) and  (r_t_2x not in self.__player_1_cords) and (r_t not in self.__player_2_cords) and (0 <= cord[0] + 2 <= 7) and (r_t in self.__player_1_cords):
                            moves_list.append(r_t_2x)
                    # Check if position at 2 left and 2 up is valid
                    if (l_t_2x not in self.__player_2_cords) and (l_t_2x not in self.__player_1_cords) and (l_t not in self.__player_2_cords) and (0 <= cord[0] - 2 <= 7) and (l_t in self.__player_1_cords):
                        moves_list.append(l_t_2x)
        return moves_list

    def __check_king(self, cord):
        """Checks and validates all possible moves for a given king piece"""
        moves_list = self.__check_men(cord)
        
        if self.__current_player == "p1":
                r_t = (cord[0] + 1, cord[1] - 1)
                l_t = (cord[0] - 1, cord[1] - 1)
                r_t_2x = (cord[0] + 2, cord[1] - 2)
                l_t_2x = (cord[0] - 2, cord[1] - 2)
                if (cord[0] <= 7) and (cord[0] >= 0) and (cord[1] <= 7):
                    # Check if position at 1 right and 1 up is valid
                    if (r_t not in self.__player_2_cords) and (r_t not in self.__player_1_cords) and (0 <= (cord[0] + 1) <= 7):
                        moves_list.append(r_t)
                    # Check if position at 1 left and 1 up is valid
                    if (l_t not in self.__player_2_cords) and (l_t not in self.__player_1_cords) and (0 <= (cord[0] - 1) <= 7):
                            moves_list.append(l_t)
                    # Check if position at 2 right and 2 up is valid
                    if (r_t_2x not in self.__player_2_cords) and  (r_t_2x not in self.__player_1_cords) and (r_t not in self.__player_1_cords) and (0 <= cord[0] + 2 <= 7) and (r_t in self.__player_2_cords):
                            moves_list.append(r_t_2x)
                    # Check if position at 2 left and 2 up is valid
                    if (l_t_2x not in self.__player_2_cords) and (l_t_2x not in self.__player_1_cords) and (l_t not in self.__player_1_cords) and (0 <= cord[0] - 2 <= 7) and (l_t in self.__player_2_cords):
                        moves_list.append(l_t_2x)

        if self.__current_player == "p2":
                r_d = (cord[0] + 1, cord[1] + 1)
                l_d = (cord[0] - 1, cord[1] + 1)
                r_d_2x = (cord[0] + 2, cord[1] + 2)
                l_d_2x = (cord[0] - 2, cord[1] + 2)
                if (0 <= cord[0] <= 7) and (cord[1] <= 7):
                    # Check if position at 1 right and 1 down is valid
                    if r_d not in self.__player_2_cords and r_d not in self.__player_1_cords and 0 <= cord[0] + 1 <= 7:
                        moves_list.append(r_d)
                    # Check if position at 1 left and 1 down is valid
                    if l_d not in self.__player_2_cords and l_d not in self.__player_1_cords and 0 <= cord[0] - 1 <= 7:
                         moves_list.append(l_d)
                    # Check if position at 2 right and 2 down is valid
                    if r_d_2x not in self.__player_1_cords and r_d_2x not in self.__player_2_cords and r_d not in self.__player_2_cords and 0 <= cord[0] + 2 <= 7 and r_d in self.__player_1_cords:
                         moves_list.append(r_d_2x)
                    # Check if position at 2 left and 2 down is valid
                    if l_d_2x not in self.__player_1_cords and  l_d_2x not in self.__player_2_cords and l_d not in self.__player_2_cords and 0 <= cord[0] - 2 <= 7 and l_d in self.__player_1_cords:
                        moves_list.append(l_d_2x)
        return moves_list

    def return_selection(self):
        """Return the click selection index if it is current_player_cords list"""
        # Checks if current player is player 1
        if self.__current_player == "p1":
            if self.select_cord in self.__player_1_cords:
                return self.__player_1_cords.index(self.select_cord)
        # Checks if current player is player 2
        elif self.__current_player == "p2":
            if self.select_cord in self.__player_2_cords:
                return self.__player_2_cords.index(self.select_cord)
        return None

    def return_valid_options(self):
         """Returns the player coordinates at the index of the click selection"""
         if self.return_selection() is not None:
              return self.check_options()[self.return_selection()]
         return []
    
    def __render_valid_options(self, surface):
         """Renders a green circle indicator at each position in the valid options list"""
         for cord in self.return_valid_options():
              x = (cord[0] * self.__square_space[0]) + self.__square_space[0] / 2
              y = (cord[1] * self.__square_space[0]) + self.__square_space[0] / 2
              draw.circle(surface, self.__colors["indicator"], (x, y), 5)
    
    def eval_winner(self):
        """Checks for a winning player on every game loop"""
        if not self.__player_2_cords:
            self.lch["winner"] = "black(p1)"
        elif not self.__player_1_cords:
            self.lch["winner"] = "white(p2)"
    
         

    def get_player_2_cords(self):
        return self.__player_2_cords

    def get_player_1_cords(self):
        return self.__player_1_cords

    def get_life_cycle_hook(self):
         return self.lch

        



        
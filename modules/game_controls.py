from pygame import draw

class GameControls:
    def __init__(self,  sqaure_space, black_checkers, white_checkers) -> None:
        self.__square_space = sqaure_space
        self.__colors = {"p1": "#d70000", "p2": "#0229bf", "indicator":"#2db83d"}
        self.__current_player = "p1"
        self.__players = {"p1": black_checkers, "p2": white_checkers}
        self.__player_1_cords = self.__players["p1"].get_pos()
        self.__player_2_cords = self.__players["p2"].get_pos()
        self.__player_1_types = self.__players["p1"].all_pieces
        self.__player_2_types = self.__players["p2"].all_pieces
        self.lch = {"p1": {"selected": False,"moved": False}, "p2": {"selected": False, "moved": False}, "winner": None}
        self.select_cord = None
        self.current_player_cords = self.__players[self.__current_player].get_pos()

    
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
         self.__current_player = player

    def get_current_player(self):
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
                # if self.__player_1_types[count] == "man":


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
                    """Check if position at 1 right and 1 down is valid"""
                    if r_d not in self.__player_2_cords and r_d not in self.__player_1_cords and 0 <= cord[0] + 1 <= 7:
                        moves_list.append(r_d)
                    """Check if position at 1 left and 1 down is valid"""
                    if l_d not in self.__player_2_cords and l_d not in self.__player_1_cords and 0 <= cord[0] - 1 <= 7:
                         moves_list.append(l_d)
                    """Check if position at 2 right and 2 down is valid"""
                    if r_d_2x not in self.__player_1_cords and r_d_2x not in self.__player_2_cords and r_d not in self.__player_1_cords and 0 <= cord[0] + 2 <= 7 and r_d in self.__player_2_cords:
                         moves_list.append(r_d_2x)
                    """Check if position at 2 left and 2 down is valid"""
                    if l_d_2x not in self.__player_1_cords and  l_d_2x not in self.__player_2_cords and l_d not in self.__player_1_cords and 0 <= cord[0] - 2 <= 7 and l_d in self.__player_2_cords:
                        moves_list.append(l_d_2x)
        
        
        if self.__current_player == "p2":
                r_t = (cord[0] + 1, cord[1] - 1)
                l_t = (cord[0] - 1, cord[1] - 1)
                r_t_2x = (cord[0] + 2, cord[1] - 2)
                l_t_2x = (cord[0] - 2, cord[1] - 2)
                if cord[0] <= 7 and cord[0] >= 0 and (cord[1] <= 7):
                    """Check if position at 1 right and 1 up is valid"""
                    if (r_t not in self.__player_2_cords) and (r_t not in self.__player_1_cords) and (0 <= (cord[0] + 1) <= 7):
                        moves_list.append(r_t)
                    """Check if position at 1 left and 1 up is valid"""
                    if (l_t not in self.__player_2_cords) and (l_t not in self.__player_1_cords) and (0 <= (cord[0] - 1) <= 7):
                            moves_list.append(l_t)
                    """Check if position at 2 right and 2 up is valid"""
                    if (r_t_2x not in self.__player_2_cords) and  (r_t_2x not in self.__player_1_cords) and (r_t not in self.__player_2_cords) and (0 <= cord[0] + 2 <= 7) and (r_t in self.__player_1_cords):
                            moves_list.append(r_t_2x)
                    """Check if position at 2 left and 2 up is valid"""
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
                    """Check if position at 1 right and 1 down is valid"""
                    if r_d not in self.__player_2_cords and r_d not in self.__player_1_cords and 0 <= cord[0] + 1 <= 7:
                        moves_list.append(r_d)
                    """Check if position at 1 left and 1 down is valid"""
                    if l_d not in self.__player_2_cords and l_d not in self.__player_1_cords and 0 <= cord[0] - 1 <= 7:
                         moves_list.append(l_d)
                    """Check if position at 2 right and 2 down is valid"""
                    if r_d_2x not in self.__player_1_cords and r_d_2x not in self.__player_2_cords and r_d not in self.__player_2_cords and 0 <= cord[0] + 2 <= 7 and r_d in self.__player_1_cords:
                         moves_list.append(r_d_2x)
                    """Check if position at 2 left and 2 down is valid"""
                    if l_d_2x not in self.__player_1_cords and  l_d_2x not in self.__player_2_cords and l_d not in self.__player_2_cords and 0 <= cord[0] - 2 <= 7 and l_d in self.__player_1_cords:
                        moves_list.append(l_d_2x)
        return moves_list

    def return_selection(self):
        """Return the click selection if it is current_player_cords"""
        if self.__current_player == "p1":
            if self.select_cord in self.__player_1_cords:
                return self.__player_1_cords.index(self.select_cord)
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
    
    # def check_winner(self):
    #      if not self.__player_1_cords:
    #           self.lch["winner"] = "White(p2)"
    # elif not self.__player_2_cords:


    def get_player_2_cords(self):
        return self.__player_2_cords

    def get_player_1_cords(self):
        return self.__player_1_cords

    def get_life_cycle_hook(self):
         return self.lch

        
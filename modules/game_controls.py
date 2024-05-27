from pygame import draw

class GameControls:
    def __init__(self,  sqaure_space, black_checkers, white_checkers) -> None:
        self.__square_space = sqaure_space
        self.__colors = {"p1": "#d70000", "p2": "#0229bf", "indicator":"#2db83d"}
        self.__current_player = "p1"
        self.__players = {"p1": black_checkers, "p2": white_checkers}
        self.__player_1_cords = self.__players["p1"].get_pos()
        self.__player_2_cords = self.__players["p2"].get_pos()
        self.lch = {"p1": {"selected": False,"moved": False}, "p2": {"selected": False, "moved": False}}
        self.select_cord = None
        self.current_player_cords = self.__players[self.__current_player].get_pos()

    
    def render_selection(self,surface):
        if self.select_cord:
                if self.__current_player == "p1":
                    if self.select_cord in self.__player_1_cords:
                        self.__render_valid_options(surface)
                        pos = (self.select_cord[0] * self.__square_space[0], self.select_cord[1] * self.__square_space[0])
                        draw.rect(surface, self.__colors[self.__current_player], [pos, self.__square_space], 3)
                
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
        all_moves = []
        moves_list = []
        if self.__current_player == "p1":
            for cord in self.__player_1_cords:
                moves_list = self.__check_men(cord)
                all_moves.append(moves_list)

        elif self.__current_player == "p2":
            for cord in self.__player_2_cords:
                moves_list = self.__check_men(cord)
                all_moves.append(moves_list)
            
        return all_moves
    
    def __check_men(self, cord):
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
                if 0 <= cord[0] <= 7 and cord[1] <= 7:
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
         """Return the player coordinates at the index of the click selection"""
         if self.return_selection():
              return self.check_options()[self.return_selection()]
         return []
    
    def __render_valid_options(self, surface):
         """Render a green circle indicator at each position in the valid options list"""
         for cord in self.return_valid_options():
              x = (cord[0] * self.__square_space[0]) + self.__square_space[0] / 2
              y = (cord[1] * self.__square_space[0]) + self.__square_space[0] / 2
              draw.circle(surface, self.__colors["indicator"], (x, y), 5)
        
    def update_player(self):

        if self.lch["p2"]["moved"]:
             self.lch["p1"]["moved"] = not self.lch["p1"]["moved"]
             self.lch["p2"]["selected"] = False
             self.__current_player = "p1"

        if self.lch["p1"]["moved"]:
             self.lch["p2"]["moved"] = not self.lch["p2"]["moved"]
             self.lch["p1"]["selected"] = False
             self.__current_player = "p2"



    # def handle_rotation(self, surface):
    #     if self.__current_player == "p1":
    #         self.render_selection(surface)
    #         print(self.lch)
    #         if self.return_selection():
    #             print(self.current_player_cords[self.return_selection()])
    #         if self.select_cord in self.current_player_cords:
    #             self.lch["p1"]["selected"] = True
    #         else:
    #             self.lch["p1"]["selected"] = False

    #         if self.select_cord in self.return_valid_options():
    #             print("Can select from player 1")
    #             self.current_player_cords[self.return_selection()] = self.select_cord
    #             self.lch["p1"]["moved"] = True
    #             self.update_player()
        
    #     elif self.__current_player == "p2":
    #          self.render_selection(surface)
    #          self.lch["p2"]["selected"] = True
             
    #          if self.lch["p2"]["selected"]:
    #               if self.select_cord in self.return_valid_options():
    #                    self.current_player_cords[self.return_selection()] = self.select_cord
    #                    self.lch["p2"]["moved"] = True
    #                    self.update_player()


            
             

    def get_player_2_cords(self):
        return self.__player_2_cords

    def get_player_1_cords(self):
        return self.__player_1_cords

    def get_life_cycle_hook(self):
         return self.lch

        
from pygame import draw

class GameControls:
    def __init__(self,  sqaure_space, black_checkers, white_checkers) -> None:
        self.__square_space = sqaure_space
        self.__colors = {"p1": "#d70000", "p2": "#0229bf"}
        self.__current_player = "p1"
        self.__players = {"p1": black_checkers, "p2": white_checkers}
        self.select_cord = None
        self.current_player_cords = self.__players[self.__current_player].get_pos()
        self.__player_1_cords = self.__players["p1"].get_pos()
        self.__player_2_cords = self.__players["p2"].get_pos()
        self.return_valid_options()        

    
    def render_selection(self,surface):
        if self.select_cord:
                
                if self.select_cord in self.current_player_cords:
                    # print(self.__return_selection(), end="\r")
                    print(self.__check_options(), end="\r")
                    # print(self.__return_selection(), end="\r")
                    pos = (self.select_cord[0] * self.__square_space[0], self.select_cord[1] * self.__square_space[0])
                    draw.rect(surface, self.__colors[self.__current_player], [pos, self.__square_space], 3)



    def toggle_player(self):
        if self.__current_player == "p1":
            self.__current_player = "p2"
        self.__current_player == "p1"

    def get_current_player(self):
        return self.__current_player


    def __check_options(self):
        all_moves = []
        moves_list = []
        for cord in self.current_player_cords:
            moves_list = self.__check_men(cord)
            all_moves.append(moves_list)
        # print(all_moves)
        return all_moves
    
    def __check_men(self, cord):
        moves_list = []
        if self.__current_player == "p1":
                if (cord[0] + 1, cord[1] + 1) not in self.__player_2_cords and (cord[0] + 1, cord[1] + 1) not in self.__player_1_cords:
                    moves_list.append((cord[0] + 1, cord[1] + 1))
        return moves_list
    
    def __return_selection(self):
        if self.select_cord in self.current_player_cords:
            return self.__players[self.__current_player].get_pos().index(self.select_cord)
        return None

    def return_valid_options(self):
         if self.__return_selection():
              return self.__check_options()[self.__return_selection()]
         return []
        
from pygame import draw

class GameControls:
    def __init__(self,  sqaure_space=(50, 50)) -> None:
        self.__square_space = sqaure_space
        self.__colors = {"p1": "#d70000", "p2": "#0229bf"}
        self.select_cord = None
    
    
    def render_selection(self,surface, player="p1"):
        if self.select_cord:
            pos = (self.select_cord[0] * self.__square_space[0], self.select_cord[1] * self.__square_space[0])
            draw.rect(surface, self.__colors[player], [pos, self.__square_space], 3)
        else:
            pass

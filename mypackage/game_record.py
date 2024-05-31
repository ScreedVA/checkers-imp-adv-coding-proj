import json

class GameRecord:
    """Class which handles json game data"""
    def __init__(self) -> None:
        """Initiliazes GameRecord variables"""
        self.__file_path = "game_record.json"
    

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
        with open(self.__file_path, "w") as f:
            json.dump(data, f,  indent=1)

    def read_record(self):
        """Returns previous game data or none"""
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            # print(f"The file '{self.__file_path}' was not found")
            return None
        
    def check_record(self):
        """Returns true if previous game data exists"""
        if self.read_record():
            return True
        return False
import json
import time





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



import json

class GameRecord:
    

    def update_record(b_pos, w_pos, b_types, w_types):
        """Will update the game record json file with the most recent game data"""
        data = {
            "positions": {
                "black_pos": b_pos,
                "white_pos": w_pos
            },
            "types": {
                "black_types": b_types,
                "white_types": w_types
            }
        }
        with open("game_record.json", "w") as f:
            json.dump(data, f)
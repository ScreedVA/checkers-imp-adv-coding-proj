import json

class GameRecord:
    

    def update_record(b_c, w_c):
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
            json.dump(data, f, indent=2, separators=(',', ':'))
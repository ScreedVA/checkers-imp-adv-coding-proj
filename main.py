import modules
import pygame

"""Initializing Modules"""
black_checkers = modules.CheckerStatus(pos=[(0, 0), (2, 0), (4, 0), (6, 0), (1, 1), (3, 1), (5, 1), (7, 1), (0, 2), (2, 2), (4, 2), (6, 2)])
white_checkers = modules.CheckerStatus(pos=[(1, 7), (3, 7), (5, 7), (7, 7), (0, 6), (2, 6), (4, 6), (6, 6), (1, 5), (3, 5), (5, 5), (7, 5)])
gb = modules.GameBoard(black_checkers, white_checkers, 0.5)
img_h = modules.ImageHandler((gb.get_square_space()))
gc = modules.GameControls(gb.get_square_space(), black_checkers, white_checkers)

gb.post_init(image_handler=img_h, game_controls=gc)
# black_checker = pygame.transform.scale(pygame.Surface(img_h.get_black_checker()), (100, 100))

        



def start():
    pygame.init()
    # - return blank screen


    screen = pygame.display.set_mode(gb.get_board_size())
    clock = pygame.time.Clock()
    running = True
    

    while running:
        gb.render_board(screen)
        gc.render_selection(screen)
        # print(gc.return_valid_options())

        """Initialize variables in outer while loop"""
        selection = gc.return_selection()
        p2_cords = gc.get_player_2_cords()
        p1_cords = gc.get_player_1_cords()
        current_player = gc.get_current_player()
        valid_options = gc.return_valid_options()
        life_cycle_hook = gc.get_life_cycle_hook()
        select_cord = gc.select_cord


        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_cord = (event.pos[0] // gb.get_square_size(), event.pos[1] // gb.get_square_size())
                gc.select_cord = clicked_cord
                print(gc.check_options())
                print(f"White Player Positions: {white_checkers.pos}")
                print(f"Black Checker Positions: {black_checkers.pos}")

                """Check if its is player 1's turn to select"""
                if current_player == "p1":
                    if clicked_cord in p1_cords:
                        gc.lch["p1"]["selected"] = True
                        gc.lch["p2"]["moved"] = False

                """Check if player 1 has selected a piece and if player can move"""
                if life_cycle_hook["p1"]["selected"]:
                    if gc.select_cord in  valid_options:
                        """Initialize possible capture positions"""
                        r_d =   (select_cord[0] + 1,  select_cord[1] + 1)
                        l_d =   (select_cord[0] - 1,  select_cord[1] + 1)
                        r_t =   (select_cord[0] + 1,  select_cord[1] - 1)
                        l_t =   (select_cord[0] - 1,  select_cord[1] - 1)

                        r_d_2x =   (select_cord[0] + 2,  select_cord[1] + 2)
                        l_d_2x =   (select_cord[0] - 2,  select_cord[1] + 2)
                        r_t_2x =   (select_cord[0] + 2,  select_cord[1] - 2)
                        l_t_2x =   (select_cord[0] - 2,  select_cord[1] - 2)


                        """Check if player 1 can capture player 2's checkers"""
                        if gc.select_cord[0] == black_checkers.pos[selection][0] + 2 or  gc.select_cord[0] == black_checkers.pos[selection][0] - 2:
                            for white_checker in white_checkers.pos:
                                """Search white checkers list for the piece to be captured"""
                                if ((white_checker == r_d and gc.select_cord == r_d_2x) or (white_checker == l_d and gc.select_cord == l_d_2x) or (white_checker == r_t and gc.select_cord == r_t_2x) or (white_checker == l_t and gc.select_cord == l_t_2x)):
                                    black_checkers.captured_pieces_pos.append(white_checkers.pos.pop(white_checkers.pos.index(white_checker)))  
                                
                                    # print(f"Captrued white checker: {white_checker}")         
                                    # print(f"All caputred white checkers: {black_checkers.captured_pieces_pos}")
                        black_checkers.pos[selection] = clicked_cord
                        gc.set_current_player("p2")
                        gc.lch["p1"]["moved"] = True
                        gc.lch["p1"]["selected"] = False

                """Check if its is player 2's turn"""
                if current_player == "p2":
                    if clicked_cord in p2_cords:
                        gc.lch["p2"]["selected"] = True
                        gc.lch["p1"]["moved"] = False

                if life_cycle_hook["p2"]["selected"]:
                    if gc.select_cord in valid_options:
                        """Initialize possible capture positions"""
                        r_d = (select_cord[0] + 1,  select_cord[1] + 1)
                        l_d = (select_cord[0] - 1,  select_cord[1] + 1)
                        r_t = (select_cord[0] + 1,  select_cord[1] - 1)
                        l_t = (select_cord[0] - 1,  select_cord[1] - 1)

                        r_d_2x = (select_cord[0] + 2,  select_cord[1] + 2)
                        l_d_2x = (select_cord[0] - 2,  select_cord[1] + 2)
                        r_t_2x = (select_cord[0] + 2,  select_cord[1] - 2)
                        l_t_2x = (select_cord[0] - 2,  select_cord[1] - 2)

                        """Check if player 1 can capture player 2's checkers"""
                        if gc.select_cord[0] == white_checkers.pos[selection][0] + 2 or  gc.select_cord[0] == white_checkers.pos[selection][0] - 2:
                            for black_checker in black_checkers.pos:
                                """Search black checkers list for the piece to be captured"""
                                if ((black_checker == r_d and gc.select_cord == r_d_2x) or (black_checker == l_d and gc.select_cord == l_d_2x) or (black_checker == r_t and gc.select_cord == r_t_2x) or (black_checker == l_t and gc.select_cord == l_t_2x)):
                                    black_checkers.captured_pieces_pos.append(black_checkers.pos.pop(black_checkers.pos.index(black_checker)))  

                                    print(f"Captrued black checker: {black_checker}")         
                                    print(f"All caputred black checkers: {black_checkers.captured_pieces_pos}")

                        white_checkers.pos[selection] = clicked_cord
                        gc.set_current_player("p1")
                        gc.lch["p2"]["moved"] = True
                        gc.lch["p2"]["selected"] = False


            if event.type == pygame.QUIT:

                running = False
        
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

def start_test():
    pygame.init()
    screen = pygame.display.set_mode(gb.get_board_size())
    clock = pygame.time.Clock()
    running = True

    selected_piece = None
    valid_moves = []

    while running:
        screen.fill(gb.get_bg_color())
        gb.render_board(screen)
        gc.render_selection(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the clicked position
                mouse_x, mouse_y = event.pos
                square_x = mouse_x // gb.get_square_size()
                square_y = mouse_y // gb.get_square_size()
                clicked_cord = (square_x, square_y)

                # If no piece is selected, try to select one
                if selected_piece is None:
                    if clicked_cord in gc.current_player_cords:
                        selected_piece = clicked_cord
                        gc.select_cord = selected_piece
                        valid_moves = gc.return_valid_options()
                else:
                    # If a piece is selected, try to move it
                    if clicked_cord in valid_moves:
                        piece_index = gc.return_selection()
                        if piece_index is not None:
                            gc.current_player_cords[piece_index] = clicked_cord
                            gc.update_player()
                            selected_piece = None
                            valid_moves = []
                        else:
                            selected_piece = None
                            valid_moves = []
                    else:
                        selected_piece = None
                        valid_moves = []
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    start()





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
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                gc.select_cord = (event.pos[0] // gb.get_square_size(), event.pos[1] // gb.get_square_size())
                
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()




if __name__ == "__main__":
    start()



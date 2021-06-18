from game import board, pieces
from game.pieces import King, Player
from utils.colours import *
from utils.spritesheet import SpriteSheet
from game.board import *
import pygame

# Display Setup
pygame.init()
screen_size = (800, 800)
gameDisplay = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Chess 2')
clock = pygame.time.Clock()

# Load Assets
pieces.sprite_sheet = SpriteSheet("assets/default_pieces.png", 6, 2, (255, 0, 0))

# Game Setup
board = Board(700, (screen_size[0] - 700) / 2, (screen_size[1] - 700) / 2)
board.setup(START_FEN)


def main():
    while True:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button = event.button
                pos = pygame.mouse.get_pos()
                '''
                1 - left click
                2 - middle click
                3 - right click
                4 - scroll up
                5 - scroll down
                '''
                if button == 1:
                    board_pos = board.convert_to_board_pos(pos)
                    if board_pos is not None:  # If clicked on board
                        board.tile_clicked(board_pos)

        # Draw To Screen
        gameDisplay.fill(DARK)  # Clear Screen

        board.draw_white(gameDisplay)
        # Update Display & Clock
        pygame.display.update()
        clock.tick(60)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

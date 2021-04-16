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
board = Board(500)
board.setup(START_FEN)


def main():
    while True:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Draw To Screen
        gameDisplay.fill(DARK)  # Clear Screen

        board.draw(gameDisplay, (screen_size[0] - board.size) / 2, (screen_size[1] - board.size) / 2)

        # Update Display & Clock
        pygame.display.update()
        clock.tick(60)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

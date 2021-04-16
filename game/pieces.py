from enum import Enum
import pygame

from utils.spritesheet import SpriteSheet

sprite_sheet = None


# ENum
class Player(Enum):
    WHITE = 1
    BLACK = 2


class King(pygame.sprite.Sprite):

    def __init__(self, player):
        # Call the sprite initializer
        pygame.sprite.Sprite.__init__(self)

        # Get Image
        if player == Player.WHITE:
            self.image = sprite_sheet.images[0]
        else:
            self.image = sprite_sheet.images[1]

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

    def draw(self, screen, x, y, size):
        image = pygame.transform.scale(self.image, (size, size))
        screen.blit(image, (x, y))

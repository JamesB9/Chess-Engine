import pygame

from utils.colours import *


class SpriteSheet:
    """ Class used to grab images out of a sprite sheet. """

    def __init__(self, filename, columns, rows, background_colour):
        """Load the sheet."""
        try:
            self.sheet = pygame.image.load(filename).convert()
            self.background_colour = background_colour
            self.columns = columns
            self.rows = rows
            self.images = self.get_images()
        except pygame.error as e:
            self.sheet = None
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)

    def get_images(self):
        images = []
        size_x = self.sheet.get_width() / self.columns
        size_y = self.sheet.get_height() / self.rows

        for x in range(self.columns):
            for y in range(self.rows):
                images.append(self.get_image(x * size_x, y * size_y, size_x, size_y))

        return images

    def get_image(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sheet, (0, 0), (x, y, width, height))

        # Assuming black works as the transparent color
        image.set_colorkey(self.background_colour)

        # Return the image
        return image
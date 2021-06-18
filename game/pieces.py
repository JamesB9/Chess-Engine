from enum import Enum
import pygame

from utils.spritesheet import SpriteSheet

sprite_sheet = None


# Enum
class Player(Enum):
    WHITE = 1
    BLACK = 2


# Move Type
class MoveType(Enum):
    SLIDE = 1  # Move Pattern
    STEP = 2  # Set of Moves


def get_piece(fen_char):
    player = Player.BLACK if fen_char.islower() else Player.WHITE
    fen_char = fen_char.lower()

    if fen_char == "k":
        return King(player)
    elif fen_char == "q":
        return Queen(player)
    elif fen_char == "r":
        return Rook(player)
    elif fen_char == "b":
        return Bishop(player)
    elif fen_char == "n":
        return Knight(player)
    elif fen_char == "p":
        return Pawn(player)
    else:
        return None


class Piece(pygame.sprite.Sprite):
    def __init__(self, player):
        # Call the sprite initializer
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.image = None
        self.move_type = None
        self.moves = []

    def draw(self, screen, x, y, size):
        image = pygame.transform.scale(self.image, (size, size))
        screen.blit(image, (x, y))


class King(Piece):
    def __init__(self, player):
        # Call the sprite initializer
        Piece.__init__(self, player)

        # Get Image
        if player == Player.WHITE:
            self.image = sprite_sheet.images[0]
        else:
            self.image = sprite_sheet.images[1]

        # Moves
        self.move_type = MoveType.STEP
        self.moves = [(1, 0), (1, 1), (0, 1),
                      (-1, 0), (-1, -1), (0, -1),
                      (-1, 1), (1, -1)]

    def __str__(self):
        return "k" if self.player == Player.BLACK else "K"


class Queen(Piece):
    def __init__(self, player):
        # Call the sprite initializer
        Piece.__init__(self, player)

        # Get Image
        if player == Player.WHITE:
            self.image = sprite_sheet.images[2]
        else:
            self.image = sprite_sheet.images[3]

        self.move_type = MoveType.SLIDE
        self.moves = [(1, 0), (1, 1), (0, 1),
                      (-1, 0), (-1, -1), (0, -1),
                      (-1, 1), (1, -1)]

    def __str__(self):
        return "q" if self.player == Player.BLACK else "Q"


class Rook(Piece):
    def __init__(self, player):
        # Call the sprite initializer
        Piece.__init__(self, player)

        # Get Image
        if player == Player.WHITE:
            self.image = sprite_sheet.images[8]
        else:
            self.image = sprite_sheet.images[9]

        self.move_type = MoveType.SLIDE
        self.moves = [(1, 0), (0, 1),
                      (-1, 0), (0, -1)]

    def __str__(self):
        return "r" if self.player == Player.BLACK else "R"


class Bishop(Piece):
    def __init__(self, player):
        # Call the sprite initializer
        Piece.__init__(self, player)

        # Get Image
        if player == Player.WHITE:
            self.image = sprite_sheet.images[4]
        else:
            self.image = sprite_sheet.images[5]

        self.move_type = MoveType.SLIDE
        self.moves = [(1, 1), (-1, -1),
                      (-1, 1), (1, -1)]

    def __str__(self):
        return "b" if self.player == Player.BLACK else "B"


class Knight(Piece):
    def __init__(self, player):
        # Call the sprite initializer
        Piece.__init__(self, player)

        # Get Image
        if player == Player.WHITE:
            self.image = sprite_sheet.images[6]
        else:
            self.image = sprite_sheet.images[7]

        self.move_type = MoveType.STEP
        self.moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                      (1, 2), (-1, 2), (1, -2), (-1, -2)]

    def __str__(self):
        return "n" if self.player == Player.BLACK else "N"


class Pawn(Piece):
    def __init__(self, player):
        # Call the sprite initializer
        Piece.__init__(self, player)

        # Get Image
        if player == Player.WHITE:
            self.image = sprite_sheet.images[10]
        else:
            self.image = sprite_sheet.images[11]

        self.move_type = MoveType.STEP
        self.moves = [(0, 1)] if player == Player.BLACK else [(0, -1)]
        self.has_moved = 0

    def __str__(self):
        return "p" if self.player == Player.BLACK else "P"

from game.pieces import King, Player
from utils.colours import *

import pygame

START_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"


class Board:
    def __init__(self, size):
        self.size = size
        self.black = GREEN
        self.white = BEIGE

        self.pieces = []
        for i in range(8):
            self.pieces.append([])

    def setup(self, fen):
        sections = fen.split(" ")
        ranks = sections[0].split("/")
        row_num = 8
        for rank in ranks:
            col_num = 0
            row_num -= 1
            for char in rank:
                if char.isdigit():
                    for i in range(int(char)):
                        col_num += 1
                        self.pieces[row_num].append(" ")
                else:
                    col_num += 1
                    self.pieces[row_num].append(char)

        for x in self.pieces:
            print(x)

    def draw(self, screen, board_x, board_y):
        tile_size = int(self.size / 8)
        pos_x = -1
        for x in range(0, self.size-tile_size, tile_size):
            pos_y = 0
            pos_x += 1
            for y in range(0, self.size-tile_size, tile_size):
                # Colour
                if (int(x / tile_size) % 2 == 0 and int(y / tile_size) % 2 == 0) or (
                        int(x / tile_size) % 2 == 1 and int(y / tile_size) % 2 == 1):
                    colour = self.black
                else:
                    colour = self.white

                # Draw Tile
                rect = pygame.Rect(board_x + x, board_y + y, tile_size, tile_size)
                pygame.draw.rect(screen, colour, rect)

                # Draw Piece
                if self.pieces[pos_y][pos_x] != " ":
                    if self.pieces[pos_y][pos_x] == "k":
                        king = King(Player.WHITE)
                        king.draw(screen, board_x + x, board_y + y, tile_size)

                pos_y += 1

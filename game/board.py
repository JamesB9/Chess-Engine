from game.pieces import King, Player, get_piece, MoveType
from utils.colours import *

import pygame

START_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
PUZZLE_FEN = "5r2/pq4k1/1pp1Qn2/2bp1PB1/3R1R2/2P3P1/P6P/6K1 w - - 1 0"
TEST_FEN = "1k5r/pP3ppp/3p2b1/1BN1n3/1Q2P3/P1B5/KP3P1P/7q w - - 1 0"

class Board:
    def __init__(self, size, x, y):
        # Board Setup
        self.size = size
        self.tile_size = int(self.size / 8)
        self.pos_x = x
        self.pos_y = y
        # Colours
        self.black = GREEN
        self.white = BEIGE
        # Pieces
        self.pieces = []
        for i in range(8):
            self.pieces.append([])
        # Moves
        self.selected_tile = None
        self.valid_moves = []

    def setup(self, fen):
        sections = fen.split(" ")
        ranks = sections[0].split("/")
        row_num = 8
        for rank in ranks:
            col_num = 8
            row_num -= 1
            for char in rank:
                if char.isdigit():
                    for i in range(int(char)):
                        col_num -= 1
                        self.pieces[row_num].append(None)
                else:
                    col_num -= 1
                    self.pieces[row_num].append(get_piece(char))

    def draw_black(self, screen):
        for x in range(8):
            for y in range(8):
                # Colour
                if x % 2 != y % 2:
                    colour = self.white
                else:
                    colour = self.black

                # Draw Tile
                screen_pos_x = self.pos_x + (x * self.tile_size)
                screen_pos_y = self.pos_y + (y * self.tile_size)
                rect = pygame.Rect(screen_pos_x, screen_pos_y, self.tile_size, self.tile_size)
                pygame.draw.rect(screen, colour, rect)

                # Draw Piece
                if self.pieces[y][x] is not None:
                    self.pieces[y][x].draw(screen, screen_pos_x, screen_pos_y, self.tile_size)

                # Draw Moves
                self.draw_potential_moves(screen)

    def draw_white(self, screen):
        for x in range(8):
            for y in range(8):
                # Tile Colour
                if x % 2 == y % 2:
                    colour = self.white
                else:
                    colour = self.black

                # Draw Tile
                screen_pos_x = self.pos_x + (x * self.tile_size)
                screen_pos_y = self.pos_y + (y * self.tile_size)
                rect = pygame.Rect(screen_pos_x, screen_pos_y, self.tile_size, self.tile_size)
                pygame.draw.rect(screen, colour, rect)

                # Draw Piece
                if self.pieces[7 - y][x] is not None:
                    self.pieces[7 - y][x].draw(screen, screen_pos_x, screen_pos_y, self.tile_size)

                # Draw Moves
                self.draw_potential_moves(screen)

    def draw_potential_moves(self, screen):
        self.valid_moves = []
        if self.selected_tile is not None:
            piece = self.get_piece_at(self.selected_tile)
            if piece is not None:
                if piece.move_type == MoveType.STEP:
                    for rel_move in piece.moves:
                        move = (rel_move[0] + self.selected_tile[0], rel_move[1] + self.selected_tile[1])
                        if self.is_move_valid(self.selected_tile, move):
                            self.valid_moves.append(move)
                            pos = self.convert_to_screen_pos(move)
                            rect = pygame.Rect(pos[0] + self.tile_size / 4, pos[1] + self.tile_size / 4,
                                               self.tile_size / 2, self.tile_size / 2)
                            pygame.draw.rect(screen, BLUE, rect)

                elif piece.move_type == MoveType.SLIDE:
                    for rel_move in piece.moves:
                        for i in range(1, 8, 1):
                            move = (rel_move[0] * i, rel_move[1] * i)
                            move = (move[0] + self.selected_tile[0], move[1] + self.selected_tile[1])
                            if self.is_move_valid(self.selected_tile, move):
                                self.valid_moves.append(move)
                                pos = self.convert_to_screen_pos(move)
                                rect = pygame.Rect(pos[0] + self.tile_size / 4, pos[1] + self.tile_size / 4,
                                                   self.tile_size / 2, self.tile_size / 2)
                                pygame.draw.rect(screen, BLUE, rect)

                                if self.get_piece_at(move) is not None and self.get_piece_at(move).player != self.get_piece_at(self.selected_tile).player:
                                    break
                            else:
                                break

    def is_move_valid(self, initial_pos, move):
        if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:  # If move on board
            piece = self.get_piece_at(initial_pos)
            piece_on_move = self.get_piece_at(move)

            if piece_on_move is None or piece_on_move.player != piece.player:  # If move no on own piece
                return True

        return False

    def tile_clicked(self, tile_pos):
        print("tile clicked:", tile_pos)
        if self.selected_tile is not None:
            print("valid moves:", self.valid_moves)
            if tile_pos in self.valid_moves:
                self.move_piece(tile_pos)
                return
            elif tile_pos == self.selected_tile:
                self.selected_tile = None
                return
        self.selected_tile = tile_pos


    def move_piece(self, move):
        print("Piece Moved")
        piece = self.get_piece_at(self.selected_tile)
        self.pieces[7 - self.selected_tile[1]][self.selected_tile[0]] = None
        self.pieces[7 - move[1]][move[0]] = piece
        self.selected_tile = None


    def get_piece_at(self, pos):
        return self.pieces[7 - pos[1]][pos[0]]

    def convert_to_board_pos(self, screen_pos):
        rel_pos = (screen_pos[0] - self.pos_x, screen_pos[1] - self.pos_y)
        tile_pos = (int(rel_pos[0] / self.tile_size), int(rel_pos[1] / self.tile_size))
        if 0 <= tile_pos[0] <= 7 and 0 <= tile_pos[1] <= 7:
            return tile_pos
        return None

    def convert_to_screen_pos(self, board_pos):
        rel_pos = (int(board_pos[0] * self.tile_size), int(board_pos[1] * self.tile_size))
        screen_pos = (rel_pos[0] + self.pos_x, rel_pos[1] + self.pos_y)
        return screen_pos

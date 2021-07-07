import pygame

from .checkerPiece import Piece
from .constantVal import BLACK, NUM_OF_COLS, NUM_OF_ROWS, RED, SQUARE_SIZE, WHITE, BLANK


class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    def draw_squares(self, window):
        window.fill(BLACK)
        for row in range(NUM_OF_ROWS):
            for col in range(row % 2, NUM_OF_COLS, 2):
                pygame.draw.rect(window, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        for row in range(NUM_OF_ROWS):
            self.board.append([])
            for col in range(NUM_OF_COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(BLANK)
                else:
                    self.board[row].append(BLANK)

    def draw(self, window):
        self.draw_squares(window)
        for row in range(NUM_OF_ROWS):
            for col in range(NUM_OF_COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(window)
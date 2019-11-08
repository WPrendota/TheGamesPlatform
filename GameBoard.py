import numpy as np


class GameBoard:

    # The Game Board initialization
    def __init__(self, board_size):
        # The board creation with different values with the size of button matrix
        self.board = np.zeros((board_size, board_size))
        self.board_size = board_size
        print(self.board)

    # Return board (string)
    def __str__(self):
        return str(self.board)

    # Return board field value
    def get_value(self, x, y):
        return self.board[x][y]

    # Return board size
    def get_board_size(self):
        return self.board_size

    # Return board
    def get(self):
        return self.board

    # Mark a board field
    def set_pawn(self, position_x, position_y, pawn):
        self.board[position_x][position_y] = pawn
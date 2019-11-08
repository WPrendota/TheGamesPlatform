import random


# The computer player
class ComputerPlayer:

    # Make a move
    def set_pawn(self, game_board):
        move = random.randint(0, game_board.get_board_size() - 1), random.randint(0, game_board.get_board_size() - 1)
        return move

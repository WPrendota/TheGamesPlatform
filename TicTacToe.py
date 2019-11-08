import numpy as np
from ComputerPlayer import ComputerPlayer
from GameBoard import GameBoard


class TicTacToe:

    # The game initialization
    def __init__(self, window_title, window_geometry, board_size):
        self.winner = 0     # The winner
        self.game_board = GameBoard(board_size)  # Board creation
        self.board_size = board_size    # Board size
        self.computer_player = ComputerPlayer()     # The Computer Player

    # The game running
    def run_game(self):
        while True:
            print("(Input format: '11')")
            print("Your move:")
            move_input_raw = input()
            print(move_input_raw)

            if self.check_input_format(move_input_raw):
                human_move = (int(move_input_raw[0]), int(move_input_raw[1]))

                if self.check_input_range(human_move):
                    if self.check_next_move(human_move):
                        self.game_board.set_pawn(human_move[0], human_move[1], 1)

                        # Check if winner
                        if self.validate(-1, 1):
                            print("The winner is: {}".format(self.winner))
                            break

                        # # Check if tie
                        if not self.check_if_board_is_full:
                            if self.validate(-1, 1):
                                print("The winner is: {}".format(self.winner))
                            break

                        # Computer Player move
                        while True:
                            computer_move = self.computer_player.set_pawn(self.game_board)
                            if self.check_next_move(computer_move):
                                self.game_board.set_pawn(computer_move[0], computer_move[1], -1)
                                break

                        # Check if winner
                        if self.validate(-1,1):
                            print(self.game_board.get())
                            print("The winner is: {}".format(self.winner))
                            break
                    else:
                        print("Position taken! Please choose empty field.")
                else:
                    print("Wrong move. Try again.")
                    continue

                print(self.game_board)
            else:
                print("Wrong move. Try again.")

    # Checking input format
    def check_input_format(self, input_data):
        return True if len(input_data) == 2 else False

    # Checking move range
    def check_input_range(self, move):
        return True if self.board_size > move[0] >= 0 and self.board_size > move[1] >= 0 else False

    # Checking game board field status for the next move
    def check_next_move(self, move):
        return True if self.game_board.get_value(move[0], move[1]) == 0 else False

    # Checking if board is full
    def check_if_board_is_full(self):
        return True if 0 in self.game_board.get() else False

    def check_columns(self, player):
        # Column are rows in the transposed list
        for column in zip(*self.game_board.get()):
            if abs(self.count_character(player, column)) == 3:
                return player
            if abs(self.count_character(player, column)) == 3:
                return player

        return False

    def check_rows(self, player):
        for row in self.game_board.get():
            if abs(self.count_character(player, row)) == 3:
                return player
            if abs(self.count_character(player, row)) == 3:
                return player

        return False

    def check_diagonals(self, player):
        # Wins if there is only one type of value in the first diagonal
        # (Numpy diag returns values on diagonal of the array).
        if abs(self.count_character(player, np.diag(self.game_board.get()))) == 3:
            return player
        if abs(self.count_character(player, np.diag(self.game_board.get()))) == 3:
            return player

        # Wins if there is only one type of value in the second diagonal (Numpy diag returns values of diagonal
        # - Numpy fliplr changes values from left to right of the array).
        if abs(self.count_character(player, np.diag(np.fliplr(self.game_board.get())))) == 3:
            return player
        if abs(self.count_character(player, np.diag(np.fliplr(self.game_board.get())))) == 3:
            return player

        return False

    # Winner finding
    def validate(self, player_1, player_2):

        if self.check_columns(player_1):
            self.winner = player_1
            return True

        if self.check_columns(player_2):
            self.winner = player_2
            return True

        if self.check_rows(player_1):
            self.winner = player_1
            return True

        if self.check_rows(player_2):
            self.winner = player_2
            return True

        if self.check_diagonals(player_1):
            self.winner = player_1
            return True

        if self.check_diagonals(player_2):
            self.winner = player_2
            return True

        counter = 0
        for row in self.game_board.get():
            for value in row:
                if value == 0:
                    counter = counter + 1
        if counter == 0:
            self.winner = "Tie"
            return True

    # Count character in the word
    def count_character(self, character, word):
        return sum(character for word_character in word if character == word_character)

    def set_pawn(self, position_x, position_y, pawn):
        if not self.is_valid_move(position_x, position_y):
            raise Exception("Pawn not valid position.")
        self.game_board.get()[position_x][position_y] = pawn

    def is_valid_move(self, position_x, position_y):
        return False if int(self.game_board.get()[position_x][position_y]) == 1 or int(
            self.game_board.get()[position_x][position_y]) == 2 else True

    def has_next_move(self):
        return np.any(self.game_board.get())

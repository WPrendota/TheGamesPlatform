from TicTacToe import TicTacToe

from argparse import ArgumentParser


# Argument Parser and game chooser
class GamesPlatform:
    board_size_tic_tac_toe_game = 3

    # The Game Platform initialization
    def __init__(self):
        game_number = self.chosen_game_mode(self.args_parser())

        if game_number == 1:
            print("Welcome to The TicTacToe game.")
            ttt = TicTacToe("Tic Tac Toe Game", "190x210", self.board_size_tic_tac_toe_game)
            ttt.run_game()

        elif game_number == 2:
            print("Welcome to The Checkers game.")
            print("In the building process.")

    # The Game Platform argument parser
    def args_parser(self):
        args = ArgumentParser(description="Tic Tac Toe Game.")
        args.add_argument('-t', action="store_true", help="The TicTacToe game.")
        args.add_argument('-c', action="store_true", help="The Checkers game")

        return args.parse_args()

    # Check which game was chosen
    def chosen_game_mode(self, args):
        # Game mode chooser and running
        if args.t == True:
            return 1

        if args.c == True:
            return 2
        else:
            print("Please choose a game mode:")
            print("-t for The TicTacToe game.")
            print("-c for The Checkers game (In the building process).")
            return 0


if __name__ == '__main__':
    ttt = GamesPlatform()

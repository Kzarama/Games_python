import re
from alpha_beta import mini_max_ab, is_game_over, mini_max
from art import *


_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"


class TicTacToeGame():
    def __init__(self):
        self.board = [None] * 9
        self.turn = _PLAYER
        self.is_game_over = False
        self.winner = None

    def is_over(self):
        return is_game_over(self.board)[0]

    def play(self):
        if self.turn == _PLAYER:
            self.player_turn()
            self.turn = _MACHINE
            self.winner = _PLAYER
        else:
            self.machine_turn()
            self.turn = _PLAYER
            self.winner = _MACHINE

    def player_choose_cell(self):
        print("Input empty cell bewtween 1 and 9")

        player_cell = input().strip()
        match = re.search("\d", player_cell)

        if not match:
            print("Input is not a number, please try again")

            return self.player_choose_cell()

        player_cell = int(player_cell) - 1

        if self.board[player_cell] is not None:
            print("Cell is already taken, try again")

            return self.player_choose_cell()

        return player_cell

    def player_turn(self):
        chosen_cell = self.player_choose_cell()

        self.board[chosen_cell] = _PLAYER_SYMBOL

    # TODO: Use your minimax alpha beta pruning algorithm here to set the machines turn
    def machine_turn(self):
        self.board = mini_max_ab(self.board, False, _MACHINE_SYMBOL, -1, 1)[1]

    def format_board(self):
        row0 = "|".join(
            list(map(lambda c: " " if c is None else c, self.board[0:3])))
        row1 = "|".join(
            list(map(lambda c: " " if c is None else c, self.board[3:6])))
        row2 = "|".join(
            list(map(lambda c: " " if c is None else c, self.board[6:9])))

        return "\n".join([row0, row1, row2])

    def print(self):
        print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
        print(self.format_board())
        print()

    def print_result(self):
        if is_game_over(self.board)[1] is None:
            Art = text2art("draw", "random")
            print(Art)
        else:
            Art = text2art(f'{self.winner} wins', "random")
            print(Art)

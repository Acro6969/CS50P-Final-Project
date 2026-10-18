import pytest
from project import Hangman, TicTacToe, Blackjack


def test_tictactoe_winner_rows():
    game = TicTacToe.__new__(TicTacToe)
    board_x_row = [
        ["X", "X", "X"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    assert game.check_winner(board_x_row) == "X"

    board_o_row = [
        ["1", "2", "3"],
        ["O", "O", "O"],
        ["7", "8", "9"]
    ]
    assert game.check_winner(board_o_row) == "O"


def test_tictactoe_winner_columns():
    game = TicTacToe.__new__(TicTacToe)
    board_x_col = [
        ["X", "2", "3"],
        ["X", "5", "6"],
        ["X", "8", "9"]
    ]
    assert game.check_winner(board_x_col) == "X"


def test_tictactoe_winner_diagonals():
    game = TicTacToe.__new__(TicTacToe)
    board_diag = [
        ["O", "2", "3"],
        ["4", "O", "6"],
        ["7", "8", "O"]
    ]
    assert game.check_winner(board_diag) == "O"


def test_tictactoe_winner_none():
    game = TicTacToe.__new__(TicTacToe)
    board_none = [
        ["X", "O", "X"],
        ["X", "O", "O"],
        ["O", "X", "X"]
    ]
    assert game.check_winner(board_none) is None


def test_hangman_get_random_word():
    game = Hangman.__new__(Hangman)
    game.vocabularies = {
        'animal': ["Chimpanzee", "Rhinoceros"]
    }
    word = game.get_random_word('animal')
    assert word in ["chimpanzee", "rhinoceros"]


def test_blackjack_calculate_score():
    game = Blackjack.__new__(Blackjack)
    game.new_ranks = Blackjack.new_ranks
    
    class MockCard:
        def __init__(self, value):
            self.value = value

    hand = [MockCard("Ace"), MockCard("10")]
    assert game.calculate_score(hand) == 21

    hand_multiple = [MockCard("King"), MockCard("5"), MockCard("2")]
    assert game.calculate_score(hand_multiple) == 17

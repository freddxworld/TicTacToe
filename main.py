#this will run the game
from board import Board
from game import Game
game_board = Board()
game_func = Game(game_board)
game_func.turns()
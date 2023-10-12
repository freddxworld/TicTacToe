#this will run the game
from board import Board
from game import Game
game_board = Board()
#this is how to create an instance of the board to use in the program
table = game_board.board
game_func = Game(table)
game_board.display()
while not game_func.is_board_full():
    game_func.turns()
    game_board.display()
    if game_func.check_win():
        print("yahh someone won")
        break
    if game_func.is_board_full():
        print("Tie you both lost")
        break
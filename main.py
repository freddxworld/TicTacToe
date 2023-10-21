#this will run the game
from board import Board
from game import Game

def main():
    #this will create our game board and any functions pertaining to it
    game_board = Board()
    table = game_board.board
    game_func = Game(table)
    game_board.display()

    #this will run our game until there are no more 
    while not game_func.is_board_full():
        game_func.turns()
        game_board.display()

        #checks if the X player has won
        if game_func.check_win('X'):
            print("congrats player you won!!!")
            break
        #checks if the O computer player has won
        elif game_func.check_win('O'):
            print("Computer has won!!!")
            break
        #checks if the board is full and there are no more spots
        elif game_func.is_board_full():
            print("Tie you both lost")
            break

if __name__ == "__main__":
    main()
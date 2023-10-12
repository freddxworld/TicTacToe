#this class will take charge of the AI/minmax algorithm
import random

class PlayerAI:
    def __init__(self): 
        self.taken_spot = True
    def choose_random_row(self):
        random_index = random.randint(0,2)
        return random_index
    def choose_random_col(self):
        random_index = random.randint(0,2)
        return random_index

    def computer_choice(self, board):
        self.board = board 
        from game import Game
        game_func = Game(self.board)
        while self.taken_spot:
            #get a random row from 1 - 3
            row = self.choose_random_row()
            #once you have chosen your row choose a column from that row
            column = self.choose_random_col()
            #check if the spot is taken or not 
            if game_func.is_spot_empty(row, column):
                print("computer chose (" + str(row) + "," + str(column) + ")")
                self.board[row][column] = 'O'
                print("\n----------------------------------------------------------------- \n")
                break     

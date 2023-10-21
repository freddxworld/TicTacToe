#this class will be responsible for the game so like UI and how it runs and such
import random
from player import Player
from playerAI import PlayerAI
class Game:
    def __init__(self, board):
        self.board = board
        self.fresh_start = True
        self.turn = ["start"]
        self.winner = ''
    #this will be used when the game first starts
    #to see who will go first
    def setup(self):
        choice1 = "player"
        choice2 = "computer"
        #chooses a random player to go first
        chosen = random.choice([choice1, choice2])
        print("the first turn goes to " + chosen)
        #saves that player so we can use later
        self.turn[0] = chosen
    #this method will be in charge of the turns in the game
    def turns(self):
        person = Player()
        ai = PlayerAI()
        #we can start off by checking if the list is emtpy if its empty then we can roll a dice/random int to find out who will go first 
        if self.fresh_start:
            self.setup()
            self.fresh_start = False
        #if the variable in the list is player then they make their move
        if self.turn[0] == "player":
            person.playerChoice(self.board)
            self.turn[0] = "computer"
        #else the computer goes 
        else:
            ai.computer_choice(self.board)
            self.turn[0] = "player"
    #will check if the spot that was chosen is empty
    def is_spot_empty(self, row, col):
        self.row = row
        self.col = col
        return self.board[self.row][self.col] == ' '
    #this will check wether someone has won
    def check_win(self, player):
        # Check rows
        for row in self.board:
            if row.count(player) == 3:
                return True
        # Check columns
        for col in range(3):
            if [self.board[row][col] for row in range(3)].count(player) == 3:
                return True
        # Check diagonals
        if [self.board[i][i] for i in range(3)].count(player) == 3 or [self.board[i][2-i] for i in range(3)].count(player) == 3:
            return True
        return False
    #will check if the game cant go on anymore cause the board is full
    def is_board_full(self):
        #so the "all" part is essential to this cause it checks it all before letting
        #you know wether its true or false
        return all(col != ' ' for row in self.board for col in row)
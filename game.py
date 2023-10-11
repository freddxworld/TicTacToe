#this class will be responsible for the game so like UI and how it runs and such
class Game:
    def __init__(self, board, row, col):
        self.board = board
        self.row = row
        self.col = col
    def setup(self):
        pass
    def turns(self):
        pass
    #will check if the spot that was chosen is empty
    def is_spot_empty(self):
        return self.board[self.row][self.col] == ' '
    #this will check wether someone has won
    def check_win(self):
        #were gonna leave out the winner variable for rn and we will figure it out later
       #self.winner = winner
        #checks each row in the table
        for rowSpot in self.board:
            if rowSpot[0] == rowSpot[1] == rowSpot[2] != ' ':
                return True
        #checks each col
        for col in range(len(self.board[0])):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return True
       #checks the diagonal 
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ' or self.board[2][0] == self.board[2][2] == self.board[0][2] != ' ':
            return True
        return False
    #will check if the game cant go on anymore cause the board is full
    def is_board_full(self):
        #so the "all" part is essential to this cause it checks it all before letting
        #you know wether its true or false
        return all(col != ' ' for row in self.board for col in row)
#setup 
#turns
#isspotempty
#check win
#is board full
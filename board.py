 #this will take care of the board for the game
class Board:
#calling Board() will use this function and will initate itself
    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
#this will display our board with vertical and horizantle lines
    def display(self):
        #this will display the numbers to know what spot to choose
        print(' | '.join(str(i) for i in range(3)))
        print('----------')
        for i, row in enumerate(self.board):
            print(' | '.join(row) + f' | {i}')
            if i < len(self.board) - 1:
                print('----------')